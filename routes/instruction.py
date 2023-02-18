from flask import Blueprint, render_template, request, redirect, session

instruction = Blueprint("instruction", __name__)


@instruction.before_request
def before_request():
    if "username" not in session:
        return redirect("/login")


@instruction.route("/instruction", methods=["GET"])
def show_strategies():
    return render_template("instruction.html", username=session.get("username"))
