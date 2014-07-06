from flask import Blueprint, request, render_template, redirect, session, flash
from utils import protect
import database

register = Blueprint(__name__, "register")

@register.route("/register/", methods=["GET", "POST"])
def page():
    if "login" in register:
        return redirect("/")

    if request.method == "POST":
        username = reqeust.form['username']
        password = protect(request.form['password'])
        confirm = protect(request.form['cpassword'])
        email = request.form['email']
        dob = request.form['dob']
        referral = request.form['referral']
        if password != confirm:
            flash("Passwords did not match.")
            return redirect("/register/")
        
        else:
            message = database.register(username, password, email, dob, referral)
            if not message['success']:
                flash(message['message'])
                return redirect("/register/")
            else:
                session['login'] = username
                return redirect("/")

    return render_template("register.html")
