import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="erosCRM",
    user="root",
    password="991155"
)
cur = conn.cursor()


def get_user_id(login, password):
    sql = """SELECT * FROM users WHERE login = %s"""
    data = (login,)
    cur.execute(sql, data)
    result = cur.fetchone()
    if result:
        return result
    return -1


def auth_user(login, password):
    if get_user_id(login, password) != -1:
        return get_user_id(login, password)
    sql = """
    INSERT INTO users (login, password)
    VALUES (%s, %s)
    """
    data = (login, password)
    cur.execute(sql, data)
    conn.commit()
    return get_user_id(login, password)


def add_company(owner_id, name, api_key, client_id):
    sql = """INSERT INTO ozon_companies (owner_id, name, api_token, client_id) VALUES (%s, %s, %s, %s)"""
    data = (owner_id, name, api_key, client_id)
    cur.execute(sql, data)
    conn.commit()


def get_companies(owner_id):
    sql = """SELECT * FROM ozon_companies WHERE owner_id = %s"""
    data = (owner_id,)
    cur.execute(sql, data)
    companies = cur.fetchall()
    d = []
    for i in companies:
        print(i)
        d.append({'owner_id': i[0], 'name': i[1], 'api_token': i[2], 'client_id': i[3]})
    return d

def insert_product():
    pass


def get_products():
    pass


def delete_company():
    pass


def stop_company():
    pass

