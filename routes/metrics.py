from flask import Blueprint, render_template, request, redirect, session

metrics = Blueprint("metrics", __name__)


@metrics.before_request
def before_request():
    if "username" not in session:
        return redirect("/login")


@metrics.route("/account-info", methods=["GET"])
def show_strategies():
    return render_template("metrics.html", username=session.get("username"))
