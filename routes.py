from server import app
from flask import render_template, redirect, flash, url_for, abort, request
from models import User
from form import RegistFrom, LoginForm

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods = ["POST","GET"])
def login():
    form_ = LoginForm()
    if form_.validate_on_submit():
        print(form_.username.data, form_.password.data)
        return redirect(url_for("index"))
    
    return render_template("login.html",form=form_)

@app.route("/register", methods = ["POST","GET"])
def register():
    form_ = RegistFrom()
    if form_.validate_on_submit():
        return redirect(url_for('login'))
    return render_template("register.html",form=form_)