from flask import Flask, render_template, request, session
from encrypt import encrypt, get_form
from queries import chat_insert, to_chat_insert, login_data
from dotenv import load_dotenv
import os
import db
import datetime


app = Flask(__name__)
load_dotenv()
# print(os.getenv('SECTET_KEY'))
# app.config["SECRET_KEY"] = os.getenv("SECTET_KEY")
app.config["SECRET_KEY"] = "jmsehdgkjsrhgjrg"

@app.route("/")
def index():
    session['login_'] = None
    session['chat_user'] = None
    return render_template('index.html', user_list=None, login=None)


@app.route("/user")
def user():
    user_list = db.do(login_data, [session['login_']])
    return render_template('index.html', user_list=user_list, login=session['login_'])


@app.route("/users", methods=["POST", "GET"])
def users():
    users_list = db.do('''SELECT * FROM users''')
    if request.method == "POST":
        session['chat_user'] = request.form.get("chat_btn")
        login_list = db.do(login_data, [session['login_']])
        user_list = db.do(login_data, [session['chat_user']])
        if session['login_'] != None:
            msg_list = db.do('''SELECT * FROM chat WHERE user_id = ? AND to_user_id = ?''', [login_list[0][0], user_list[0][0]])
            return render_template("chat.html", user_list=user_list, login=session['login_'], msg_list=msg_list)
        return render_template("login.html", error="You need to log in")
    return render_template('users.html', users_list=users_list, login=session['login_'])


@app.route("/registration", methods=["POST", "GET"])
def registration():
    if request.method == "POST":
        form_dict = get_form(request.values.lists())
        session['login_'] = form_dict['login']
        data = db.do(login_data, [session['login_']])
        if not data:
            if form_dict['password'] == form_dict['password_commit']:
                db.insert_new(form_dict)
            else:
                return render_template("registration.html", error="password")
            data = db.do(login_data, [session['login_']])
            return render_template("index.html", login=session['login_'], user_list=data)
        return render_template("registration.html", error="login is already exist")
    return render_template("registration.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session['login_'] = request.form.get("login")
        password = encrypt(request.form.get("password"))
        data = db.do(login_data, [session['login_']])
        if not data:
            return render_template("login.html", error="login has not been found")
        else:
            if password == data[0][7]:
                return render_template("index.html", login=session['login_'], user_list=data)
            return render_template("login.html", error="uncorrect password")
    return render_template("login.html")


@app.route("/chat", methods=["POST", "GET"])
def chat():
    login_list = db.do(login_data, [session['login_']])
    user_list = db.do(login_data, [session['chat_user']])
    msg_list = db.do('''SELECT * FROM chat WHERE user_id = ? AND to_user_id = ?''', [login_list[0][0], user_list[0][0]])
    if request.method == "POST":
        text = request.form.get("write_message")
        msg_datetime = datetime.datetime.now()
        if len(text) != 0:
            print('text')
            db.do(chat_insert, [login_list[0][0], user_list[0][0], text, msg_datetime])
            db.do(to_chat_insert, [user_list[0][0], login_list[0][0], text, msg_datetime])
            msg_list = db.do('''SELECT * FROM chat WHERE user_id = ? AND to_user_id = ?''', [login_list[0][0], user_list[0][0]])
            # return render_template("chat.html", login=session['login_'], user_list=user_list, msg_list=msg_list)
        # return render_template("chat.html", login=session['login_'], user_list=user_list, msg_list=msg_list)
    return render_template("chat.html", login=session['login_'], user_list=user_list, msg_list=msg_list)


app.run(debug=True)