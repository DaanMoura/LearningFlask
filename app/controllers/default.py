from flask import render_template, flash, redirect, url_for
import flask_login as fl
from app import app, db, lm

from app.models.tables import User
from app.models.forms import LoginForm

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

#rota para o index (home)
@app.route("/u/<user>")
@app.route("/index")
@app.route("/", defaults={"user":None})
def index(user):
    return render_template("index.html", user=user)

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            fl.login_user(user)
            return redirect(url_for("index"))
            # flash("Logged in")
            print("Logged in")
        else:
            # flash("Invalid Login")
            print("Invalid Login")

    else:
        print(form.errors)
    return render_template('login.html', form=form)

# Not render a template, it is just a function for logout
@app.route("/logout")
def logout():
    fl.logout_user()
    # flash("Logged out")
    print("Logged out")
    return redirect(url_for("index"))

@app.route("/posts")
def posts():
    return render_template("posts.html")
