from flask import Blueprint, request, render_template, redirect, session, flash
from utils import protect
import database

login = Blueprint(__name__, "login")

@login.route("/login/", methods=['GET', 'POST'])
def page():
    if "login" in session:
        return redirect("/")

    if request.method == "POST":
        username = request.form['username']
        password = protect(request.form['password'])

        check = database.getUser(username)
        if not check:
            flash("Username invalid")
            return redirect("/login/")
        elif check['password'] != password:
            flash("Password invalid")
            return redirect("/login/")
        else:
            session['login'] = username
            return redirect("/")


    return render_template("login.html")
