from flask import Blueprint, flash, render_template, redirect, request
import database

threaddisplay = Blueprint(__name__, "threaddisplay")

@threaddisplay.route("/thread/<section>/<_id>")
def post(section, _id):
    if "login" not in session:
        return redirect("/")

    thread = database.getThread(section, _id)
    posts = database.getPosts(_id)

    return render_template("threaddisplay.html", thread=thread, posts=posts)
