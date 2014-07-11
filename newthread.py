from flask import Blueprint, redirect, render_template, request, flash, session
import database

newthread = Blueprint(__name__, "newthread")

@newthread.route("/newthread/<section>",methods=["GET","POST"])
def page(section):
    if "login" not in session:
        return redirect("/")
    
    if request.method == "POST":
        title = request.form['title']
        message = request.form['message']
        database.makeThread(session['login'], message, section, title)
        #flash("Post made") Don't need a flash as they won't see it anyways
        return redirect("/newthread/{0}".format(section))

    return render_template("newthread.html")

