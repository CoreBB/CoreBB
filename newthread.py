from flask import Blueprint, redirect, render_template, request, flash
import database

newthread = Blueprint(__name__, "newthread")

@newthread.route("/newthread/<section>")
def page(section):
    if "login" not in session:
        return redirect("/")
    
    if request.method == "POST":
        title = request.form['title']
        body = request.form['body']
        database.makeThread(session['login'], body, section, title)
        flash("Post made")
        return redirect("/newthread/{0}".format(section))

    return render_template("newthread.html")

