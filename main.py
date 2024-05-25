from flask import Flask, render_template, redirect, request, session
from core.functions.get_register_form import get_form
from core.functions.encrypt import encrypt
from core.functions.msg import get_msg_list, update_msg_list, get_unread_msg
from core.utils.settings import settings
from core.db.queries import login_data, id_data
import core.db.scripts as db


app = Flask(__name__)
app.config["SECRET_KEY"] = settings.key


@app.route("/")
def index():
    session['login'] = None
    session['chat_id'] = None
    return render_template('index.html')


@app.route("/user", methods=["POST", "GET"])
def user():
    user_list = db.do(login_data, [session['login']])
    notice_list = get_unread_msg(user_list[0][0])
    if request.method == "POST":
        session['chat_id'] = request.form.get("chat_btn")
        return redirect("/chat")
    return render_template('user.html', user_list=user_list, login=session['login'], notice=notice_list)


@app.route("/users", methods=["POST", "GET"])
def users():
    users_list = db.do('''SELECT * FROM users''')
    if request.method == "POST":
        session['chat_id'] = request.form.get("chat_btn")
        if session['login'] != None:
            return redirect("/chat")
        return render_template("login.html", error="Вам нужно войти.")
    return render_template('users.html', users_list=users_list, login=session['login'])


@app.route("/registration", methods=["POST", "GET"])
def registration():
    if request.method == "POST":
        form_dict = get_form(request.values.lists())
        if not form_dict:
            return render_template("registration.html", error="Пустое поле ввода.")
        session['login'] = form_dict['login']
        data = db.do(login_data, [session['login']])
        if not data:
            if form_dict['password'] == form_dict['password_commit']:
                db.insert_new(form_dict)
            else:
                return render_template("registration.html", error="Пароли не совпадают.")
            return redirect("/user")
        return render_template("registration.html", error="Логин уже существует.")
    return render_template("registration.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session['login'] = request.form.get("login")
        password = encrypt(request.form.get("password"))
        data = db.do(login_data, [session['login']])
        if not data:
            return render_template("login.html", error="Логин не был найден.")
        else:
            if password == data[0][7]:
                return redirect("/user")
            return render_template("login.html", error="Неверный пароль.")
    return render_template("login.html")


@app.route("/chat", methods=["POST", "GET"])
def chat():
    user_list = db.do(id_data, [session['chat_id']])
    msg_list = get_msg_list(session['login'], session['chat_id'])
    if request.method == "POST":
        text = request.form.get("write_message")
        if len(text) != 0:
            update_msg_list(session['login'], session['chat_id'], text)
            return redirect('/chat')
    return render_template("chat.html", login=session['login'], user_list=user_list, msg_list=msg_list)


app.run(debug=True)