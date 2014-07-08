from flask import Blueprint, request, render_template, redirect, session

index = Blueprint("index", __name__)

@index.route("/", methods=["GET", "POST"])
def page():
    return render_template("index.html")
