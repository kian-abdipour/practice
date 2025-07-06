from fastapi.testclient import TestClient

from restaurant.main import app


client = TestClient(app)


def test_addition_item_to_cart():
    # 1_Addition item to cart successful
    header = {'customer-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUsInJvbGUiOiJjdXN0b21lciIsInVzZXJuYW1lIjoibWF0aW4iLCJleHAiOjE3NzUxNjU3NTZ9.fu6HdZ_wKF6EYWfHm704rd831mKO8fjIWykFi_Nc85c'}
    item = {'item_id': 3}

    response = client.post('/carts', headers=header, json=item)

    assert response.status_code == 200

    # 2_Addition not existed item to cart
    item = {'item_id': 999}

    response = client.post('carts', headers=header, json=item)

    assert response.status_code == 404

    # 3_Addition item that is out of stock
    item = {'item_id': 13}

    response = client.post('carts', headers=header, json=item)

    assert response.status_code == 400

    # 4_Addition item that is already added to cart
    item = {'item_id': 3}

    response = client.post('/carts', headers=header, json=item)

    assert response.status_code == 409


def test_get_items_in_customer_cart():
    # 1_Get all items in customer cart successful to get 200
    header = {'customer-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUsInJvbGUiOiJjdXN0b21lciIsInVzZXJuYW1lIjoibWF0aW4iLCJleHAiOjE3NzUxNjU3NTZ9.fu6HdZ_wKF6EYWfHm704rd831mKO8fjIWykFi_Nc85c'}

    response = client.get('/carts/items', headers=header)

    assert response.status_code == 200

    # 2_Get all items in customer cart with order_by
    order_by = {'order_by': ['id']}

    response = client.get('/carts/items', headers=header, params=order_by)

    assert response.status_code

    # 3_Get all items in customer cart with wrong order_by
    order_by = {'order_by': ['Somthing that is not in item rows']}

    response = client.get('/carts/items', headers=header, params=order_by)

    assert response.status_code == 400


def test_update_quantity():
    # 1_Update quantity successful to get 200 >>> increase
    header = {'customer-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUsInJvbGUiOiJjdXN0b21lciIsInVzZXJuYW1lIjoibWF0aW4iLCJleHAiOjE3NzUxNjU3NTZ9.fu6HdZ_wKF6EYWfHm704rd831mKO8fjIWykFi_Nc85c'}
    body = {'item_id': 3, 'quantity': 1}

    response = client.put('/carts', headers=header, json=body)

    assert response.status_code == 200

    # 2_Update quantity successful to get 200 >>> decrease
    body = {'item_id': 3, 'quantity': -1}

    response = client.put('/carts', headers=header, json=body)

    assert response.status_code == 200

    # 3_Update quantity by wrong id
    body = {'item_id': 999, 'quantity': 1}

    response = client.put('/carts', headers=header, json=body)

    assert response.status_code == 404

    # 4_Update an item that is out of stock
    body = {'item_id': 12, 'quantity': 1}

    response = client.put('/carts', headers=header, json=body)

    assert response.status_code == 400

    # 5_Update an item that is not in customer cart
    body = {'item_id': 11, 'quantity': 1}

    response = client.put('/carts', headers=header, json=body)

    assert response.status_code == 404

    # 6_Update an item with wrong quantity
    body = {'item_id': 3, 'quantity': 999}

    response = client.put('/carts', headers=header, json=body)

    assert response.status_code == 400


def test_delete_item():
    # 1_Delete item from cart to get 200
    header = {'customer-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUsInJvbGUiOiJjdXN0b21lciIsInVzZXJuYW1lIjoibWF0aW4iLCJleHAiOjE3NzUxNjU3NTZ9.fu6HdZ_wKF6EYWfHm704rd831mKO8fjIWykFi_Nc85c'}

    response = client.delete('/carts/3', headers=header)

    assert response.status_code == 200

    # 2_Delete an item that is not in customer cart
    response = client.delete('/carts/999', headers=header)

    assert response.status_code == 404


