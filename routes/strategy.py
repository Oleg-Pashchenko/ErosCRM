from flask import Blueprint, render_template, request, redirect, session

strategy = Blueprint("strategy", __name__)


@strategy.before_request
def before_request():
    if "username" not in session:
        return redirect("/login")


@strategy.route("/strategies", methods=["GET"])
def show_strategies():
    return render_template("strategies.html", username=session.get("username"))
