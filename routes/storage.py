from flask import Blueprint, render_template, request, redirect, session
from database import storages as st

storage = Blueprint("storage", __name__)


@storage.before_request
def before_request():
    if "username" not in session:
        return redirect("/login")


@storage.route("/storages", methods=["GET"])
def show_storages():
    return render_template("storages.html", username=session.get("username"), storages_info=st.get_storage_list())


@storage.route("/storages/add-storage", methods=["GET"])
def add_storage():
    return render_template("add-storage.html", username=session.get("username"))


@storage.route("/storages/add-storage", methods=["POST"])
def add_storage_post():
    name = request.form.get('storage-name')
    descr = request.form.get('storage-descr')
    st.create_storage_db(session.get('id'), name, descr)
    return redirect('/storages')


@storage.route("/storages/<string:name>", methods=['GET'])
def view_shop(name):
    storage_info = st.get_storage_info(name)
    storage_data = []
    return render_template('storage.html', username=session.get('username'), storage_info=storage_info,
                           storage_data=storage_data)
