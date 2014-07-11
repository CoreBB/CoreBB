from flask import Blueprint, flash, render_template, redirect, request, session
import database

threaddisplay = Blueprint(__name__, "threaddisplay")

@threaddisplay.route("/thread/<section>/<_id>", methods=['GET', 'POST'])
def post(section, _id):
    if "login" not in session:
        return redirect("/")

    thread = database.getThread(section, _id)
    posts = database.getPosts(_id)
    
    # Am I missing something?
    if request.method == "POST":
        username = thread["username"]
        content = request.form["content"]
        database.makePost(username, content, _id)
        return redirect("/thread/" + section + "/" + _id)
    else:
        return render_template("threaddisplay.html", thread=thread, posts=posts)
