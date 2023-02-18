from flask import Blueprint, render_template, request, redirect, session

index = Blueprint("index", __name__)


@index.before_request
def before_request():
    if "username" not in session:
        return redirect("/login")


@index.route("/", methods=["GET"])
def show_index():
    return render_template("index.html", username=session.get("username"))
