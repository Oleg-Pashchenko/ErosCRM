from flask import Blueprint, render_template, request, redirect, session
from database import shops as sh
shops = Blueprint("shops", __name__)


@shops.before_request
def before_request():
    if "username" not in session:
        return redirect("/login")


@shops.route("/shops", methods=["GET"])
def show_shops():
    return render_template("shops.html", username=session.get("username"), shops_info=sh.get_shop_list())


@shops.route("/shops/add-ozon", methods=['GET'])
def add_ozon():
    return render_template('add-ozon.html', username=session.get('username'))


@shops.route("/shops/add-ozon", methods=['POST'])
def add_ozon_post():
    shop_name = request.form.get('shop-name')
    shop_link = request.form.get('shop-link')
    api_token = request.form.get('api-token')
    client_id = request.form.get('client-id')
    sh.create_shop_db(session.get('id'), shop_name, shop_link, client_id, api_token)
    return redirect('/shops')


@shops.route("/shops/<string:api_token>", methods=['GET'])
def view_shop(api_token):
    shop_info = sh.get_shop_info(api_token)
    shop_data = []
    return render_template('shop.html', username=session.get('username'), shop_info=shop_info, shop_data=shop_data)

