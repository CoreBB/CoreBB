from flask import Blueprint, redirect, render_template, request, flash, session
import database

newthread = Blueprint(__name__, "newthread")

<<<<<<< HEAD
@newthread.route("/newthread/<section>",methods=["GET","POST"])
=======
@newthread.route("/newthread/<section>", methods=['GET', 'POST'])
>>>>>>> 5bc1d7f1265147a046a03d930d54b23c6d9804e7
def page(section):
    if "login" not in session:
        return redirect("/")
    
    if request.method == "POST":
        title = request.form['title']
<<<<<<< HEAD
        message = request.form['message']
        database.makeThread(session['login'], message, section, title)
        #flash("Post made") Don't need a flash as they won't see it anyways
=======
        body = request.form['message']
        database.makeThread(session['login'], body, section, title)
        flash("Post made")
>>>>>>> 5bc1d7f1265147a046a03d930d54b23c6d9804e7
        return redirect("/newthread/{0}".format(section))

    return render_template("newthread.html")

