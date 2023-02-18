from flask import Blueprint, render_template, request, redirect, session

servers = Blueprint("servers", __name__)


@servers.before_request
def before_request():
    if "username" not in session:
        return redirect("/login")


@servers.route("/servers", methods=["GET"])
def show_servers():
    return render_template("servers.html", username=session.get("username"))
