from flask import Flask, render_template, request, session
import hashlib
import db_scripts


app = Flask(__name__)
app.config["SECRET_KEY"] = "SuperUltimateVerySecretKey"


@app.route("/")
def index():
    session['login_'] = None
    return render_template('index.html', user_list=None, login=session['login_'])


@app.route("/user")
def user():
    login_ = session['login_']
    user_list = db_scripts.do(f'''SELECT * FROM users WHERE login = "{login_}"''')
    return render_template('index.html', user_list=user_list, login=session['login_'])


@app.route("/users")
def users():
    users_list = db_scripts.do('''SELECT * FROM users''')
    return render_template('users.html', users_list=users_list, login=session['login_'])


@app.route("/registration", methods=["POST", "GET"])
def registration():
    if request.method == "POST":
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        age = request.form.get('age')
        town = request.form.get('town')
        img = request.form.get('img')
        session['login_'] = request.form.get('login')
        password = request.form.get('password')
        password_commit = request.form.get('password_commit')
        login_ = session['login_']
        data = db_scripts.do(f'SELECT * FROM users WHERE login = "{login_}"')
        if not data:
            if password == password_commit:
                encrypt = hashlib.sha256()
                encrypt.update(password.encode())
                encrypted_password = encrypt.hexdigest()
                db_scripts.insert_new(fname, lname, age, town, img, session['login_'], encrypted_password)
            else:
                return render_template("registration.html", error="password")
            data = db_scripts.do(f'SELECT * FROM users WHERE login = "{login_}"')
            return render_template("index.html", login=session['login_'], user_list=data)
        return render_template("registration.html", error="login is already exist")
    return render_template("registration.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session['login_'] = request.form.get("login")
        password = request.form.get("password")
        encrypt = hashlib.sha256()
        encrypt.update(password.encode())
        encrypted_password = encrypt.hexdigest()
        login_ = session['login_']
        data = db_scripts.do(f'SELECT * FROM users WHERE login = "{login_}"')
        if not data:
            return render_template("login.html", error="login has not been found")
        else:
            if encrypted_password == data[0][6]:
                return render_template("index.html", login=session['login_'], user_list=data)
            return render_template("login.html", error="uncorrect password")
    return render_template("login.html")


app.run(debug=True)