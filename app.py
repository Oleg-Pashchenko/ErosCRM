from flask import Flask, render_template, request, redirect, session

from backend.databases.ozon import add_company, auth_user, get_companies
from backend.sites.ozon import is_api_connection_correct

app = Flask(__name__)
app.secret_key = '991155'


def user_logged_in():
    if 'username' in session:
        return True
    else:
        return False


@app.route('/', methods=["GET"])
def shops():
    if not user_logged_in(): return redirect('/login')
    companies = get_companies(session['id'])
    return render_template('shops.html', email=session['username'], shops=companies)


@app.route('/add-shop', methods=["GET"])
def add_shop():
    if not user_logged_in(): return redirect('/login')
    return render_template('add-shop.html', email=session['username'])


@app.route('/add-shop', methods=['POST'])
def handle_add_shop():
    shop_type = request.form.get('type')
    name = request.form.get('name')
    api_key = request.form.get('api_key')
    client_id = request.form.get('client_id')
    if shop_type == 'ozon':
        if is_api_connection_correct(api_key, client_id):
            add_company(session['id'], name, api_key, client_id)
    return redirect('/')


@app.route('/login', methods=["GET"])
def login():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form.get('email')
    password = request.form.get('password')  # create new user or login
    db_data = auth_user(username, password)
    if password != db_data[2]:
        return redirect('/login')
    index = db_data[0]
    session['username'] = username
    session['password'] = password
    session['id'] = index
    return redirect('/')


@app.route('/<string:owner_id>/<string:shop>', methods=["GET"])
def products(owner_id: str, shop: str):
    if not user_logged_in(): return redirect('/login')
    products = []
    for i in range(100000):
        products.append({"product_id": 1, "name": "Product 1", "description": "Description 1", "price": 100, "count": 10})
    return render_template('products.html', products=products)


if __name__ == '__main__':
    app.run()
