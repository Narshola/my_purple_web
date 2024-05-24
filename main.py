from flask import Flask, render_template, request, session, redirect
from encrypt import encrypt
from get_unread_msg import get_unread_msg
from get_register_form import  get_form
from queries import chat_insert, to_chat_insert, login_data, id_data, msg_data, get_new_msg
from dotenv import load_dotenv
from settings import get_msg_list, update_msg_list
import os
import db
from datetime import datetime


app = Flask(__name__)
load_dotenv()
app.config["SECRET_KEY"] = os.getenv("KEY")


@app.route("/")
def index():
    session['login_'] = None
    session['chat_user'] = None
    return render_template('index.html', user_list=None, login=None)


@app.route("/user", methods=["POST", "GET"])
def user():
    user_list = db.do(login_data, [session['login_']])
    msg_notice = db.do(get_new_msg, [user_list[0][0]])
    notice_list = get_unread_msg(msg_notice)
    if request.method == "POST":
        session['chat_user'] = request.form.get("chat_btn")
        msg_list = get_msg_list(session['login_'], session['chat_user'])
        msg_user_list = db.do(id_data, [session['chat_user']])
        return render_template("chat.html", user_list=msg_user_list, login=session['login_'], msg_list=msg_list)
    return render_template('user.html', user_list=user_list, login=session['login_'], notice=notice_list)


@app.route("/users", methods=["POST", "GET"])
def users():
    users_list = db.do('''SELECT * FROM users''')
    if request.method == "POST":
        session['chat_user'] = request.form.get("chat_btn")
        login_list = db.do(login_data, [session['login_']])
        user_list = db.do(id_data, [session['chat_user']])
        if session['login_'] != None:
            msg_list = get_msg_list(session['login_'], session['chat_user'])
            return render_template("chat.html", user_list=user_list, login=session['login_'], msg_list=msg_list)
        return render_template("login.html", error="You need to log in")
    return render_template('users.html', users_list=users_list, login=session['login_'])


@app.route("/registration", methods=["POST", "GET"])
def registration():
    if request.method == "POST":
        form_dict = get_form(request.values.lists())
        if not form_dict:
            return render_template("registration.html", error="an empty input")
        session['login_'] = form_dict['login']
        data = db.do(login_data, [session['login_']])
        if not data:
            if form_dict['password'] == form_dict['password_commit']:
                db.insert_new(form_dict)
            else:
                return render_template("registration.html", error="password")
            data = db.do(login_data, [session['login_']])
            return render_template("user.html", login=session['login_'], user_list=data)
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
                msg_notice = db.do(get_new_msg, [data[0][0]])
                notice_list = get_unread_msg(msg_notice)
                return render_template("user.html", login=session['login_'], user_list=data, notice=notice_list)
            return render_template("login.html", error="uncorrect password")
    return render_template("login.html")


@app.route("/chat", methods=["POST", "GET"])
def chat():
    user_list = db.do(id_data, [session['chat_user']])
    msg_list = get_msg_list(session['login_'], session['chat_user'])
    if request.method == "POST":
        text = request.form.get("write_message")
        if len(text) != 0:
            update_msg_list(session['login_'], session['chat_user'], text)
            msg_list = get_msg_list(session['login_'], session['chat_user'])
            return redirect('/chat')
    return render_template("chat.html", login=session['login_'], user_list=user_list, msg_list=msg_list)


app.run(debug=True)