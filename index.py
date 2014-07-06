from flask import Blueprint, request, render_template, redirect, session

index = Blueprint(__name__ "index")

@index.route("/", methods=["GET", "POST"])
def page():
    return render_template("index.html")
