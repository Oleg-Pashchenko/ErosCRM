from flask import Blueprint, render_template, request, redirect, session

from database import accounts

login = Blueprint("login", __name__)


@login.route("/login", methods=["GET"])
def show_login():
    return render_template("auth.html", err=False)


@login.route("/login", methods=["POST"])
def show_login_post():
    tg_code = request.form.get("tg_code")
    result = accounts.try_login(int(tg_code))
    if not result:
        return render_template("auth.html", err=True)
    session["username"] = accounts.get_info_about_user(int(tg_code)).name
    session["id"] = accounts.get_info_about_user(int(tg_code)).id
    return redirect("/")
