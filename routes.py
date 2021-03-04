from server import app
from flask import render_template, redirect, flash, url_for, abort, request
import models as md
from form import RegistFrom, LoginForm
from sqlalchemy  import exc

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods = ["POST","GET"])
def login():
    form_ = LoginForm()
    if form_.validate_on_submit():
        if(md.login(form_.username.data,form_.password.data)):

            return redirect(url_for("index"))
        else:
            flash("Warning: Wrong username or password")
            return render_template("login.html",form=form_)

    return render_template("login.html",form=form_)

@app.route("/register", methods = ["POST","GET"])
def register():
    form_ = RegistFrom()
    if form_.validate_on_submit():
        try:
            md.register(form_.username.data,form_.password.data)
            flash("Register success! Please login")
            return redirect(url_for('login'))

        except exc.IntegrityError as e:
            flash("Warning: This name has been taken!")
            return render_template("register.html",form=form_)

    return render_template("register.html",form=form_)
