import json

import requests


def is_api_connection_correct(api_key: str, client_id: str):
    headers = {
        'Content-Type': 'application/json',
        'Api-Key': api_key,
        "Client-Id": client_id
    }
    url = "https://api-seller.ozon.ru/v2/product/list"
    response = requests.post(url=url, headers=headers)
    if response.status_code != 200:
        return False
    return True


def get_products_list(api_key: str, client_id: str):
    headers = {
        'Content-Type': 'application/json',
        'Api-Key': api_key,
        'Client-Id': client_id
    }
    url = "https://api-seller.ozon.ru/v2/product/list"
    response = requests.post(url=url, headers=headers)
    if response.status_code != 200:
        return []  # TODO: Alert admin about error
    else:
        return response.json()['result']['items']


def get_product_info(api_key: str, client_id: str, product_id: int):
    url = "https://api-seller.ozon.ru/v2/product/info"
    headers = {
        'Content-Type': 'application/json',
        'Api-Key': api_key,
        'Client-Id': client_id
    }
    data = {
        "product_id": product_id
    }
    response = requests.post(url=url, headers=headers, data=json.dumps(data))
    if response.status_code != 200:
        return []  # TODO: Alert admin about error
    else:
        return response.json()['result']

test_name = ""
test_client_id = "855070"
test_api_key = 'bea0d309-0fc7-4661-a1aa-fc0d4380a011'
#print(is_api_connection_correct(test_api_key, test_client_id))
#print(get_products_list(test_api_key, test_client_id))
#print(get_product_info(test_api_key, test_client_id, 446319748))
