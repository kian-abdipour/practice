from fastapi.testclient import TestClient

from restaurant.main import app


client = TestClient(app)


def test_addition():
    # 1_Addition an item successful to get 200
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjYsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiamoiLCJleHAiOjE3NzQ5MDU3OTd9.nhq20V7Ei7ifUsTK5zWflBGv2VFYv0IC2Ge1rD2xpGI'}
    item = {
        'name': 'stake',
        'country': 'italy',
        'price': 80,
        'stock': 15,
        'category_id': 79,
        'description': 'Italiano perfectiono'
    }

    response = client.post('/items', headers=header, json=item)

    assert response.status_code == 200

    # 2_Addition an item with repeated name
    response = client.post('/items', headers=header, json=item)

    assert response.status_code == 409

    # 3_Addition an item with not existed category
    item = {
        'name': 'stake',
        'country': 'italy',
        'price': 80,
        'stock': 15,
        'category_id': 999,
        'description': 'Italiano perfectiono'
    }

    response = client.post('/items', headers=header, json=item)

    assert response.status_code == 404

    # 3_Addition an item with long name
    item = {
        'name': 'sssssssssssssssssssssssstttttttttttttttttttttttttttttttaaaaaaaaaaaaaaakkkkkkkkkkkkkkkkeeeeeeeeeeeeeee',
        'country': 'italy',
        'price': 80,
        'stock': 15,
        'category_id': 79,
        'description': 'Italiano perfectiono'
    }

    response = client.post('/items', headers=header, json=item)

    assert response.status_code == 400

    # 4_Addition an item with long country
    item = {
        'name': 'stake',
        'country': 'iiiiiiiiiiiiiiiiiiiiiiiiitttttttttttttttttttttttttaaaaaaaaaaaaaaaallllllllllllllllllyyyyyyyyyyyyyy',
        'price': 80,
        'stock': 15,
        'category_id': 79,
        'description': 'Italiano perfectiono'
    }

    response = client.post('/items', headers=header, json=item)

    assert response.status_code == 400

    # 5_Addition an item with price that is lower or equal to zero
    item = {
        'name': 'stake',
        'country': 'italy',
        'price': -30,
        'stock': 15,
        'category_id': 79,
        'description': 'Italiano perfectiono'
    }

    response = client.post('/items', headers=header, json=item)

    assert response.status_code == 400

    # 6_Addition an item with stock that is lower than zero
    item = {
        'name': 'stake',
        'country': 'italy',
        'price': 80,
        'stock': -10,
        'category_id': 79,
        'description': 'Italiano perfectiono'
    }

    response = client.post('/items', headers=header, json=item)

    assert response.status_code == 400


def test_get():
    # 1_Get all items successful
    header = {'customer-or-admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjYsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiamoiLCJleHAiOjE3NzQ5MDU3OTd9.nhq20V7Ei7ifUsTK5zWflBGv2VFYv0IC2Ge1rD2xpGI'}

    response = client.get('/items', headers=header)

    assert response.status_code == 200

    # 2_Get all items with order_by
    order_by = {'order_by': ['id']}

    response = client.get('/items', headers=header, params=order_by)

    assert response.status_code == 200

    # 3_Get an item with id
    item = {'id': 3}

    response = client.get('/items', headers=header, params=item)

    assert response.status_code == 200

    # 4_Get an item with name
    item = {'name': 'pizza'}

    response = client.get('/items', headers=header, params=item)

    assert response.status_code == 200

    # 5_Get items with wrong order_by
    order_by = {'order_by': ['Somthing that is not in item rows']}

    response = client.get('/items', headers=header, params=order_by)

    assert response.status_code == 400

    # 6_Get an item with wrong id
    item = {'id': 999}

    response = client.get('/items', headers=header, params=item)

    assert response.status_code == 404

    # 7_Get an item with wrong name
    item = {'name': 'Wrong name'}

    response = client.get('/items', headers=header, params=item)

    assert response.status_code == 404