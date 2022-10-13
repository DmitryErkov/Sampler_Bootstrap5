from app import *
from flask import render_template
from .form import LoginForm


@app.route("/")
def index():
    return render_template('index.html', title="Главная")


@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("Custom WTForms - is ok")
    return render_template('login.html', form=form, title="Авторизация")
