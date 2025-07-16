from fastapi.testclient import TestClient

from restaurant.main import app


client = TestClient(app=app)


def test_addition():
    # 1_Addition discount successful to get 200
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjYsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiamoiLCJleHAiOjE3NzQ5MDU3OTd9.nhq20V7Ei7ifUsTK5zWflBGv2VFYv0IC2Ge1rD2xpGI'}
    body = {
        'start_date': '2025-01-01',
        'expire_date': '2025-12-29',
        'title': 'New year',
        'percent': 0.2,
        'description': 'Start new year by saving money',
        'usage_limitation': 10,
        'disposable': True,
        'one_use': True
    }

    response = client.post('/discounts', headers=header, json=body)

    assert response.status_code == 200

    # 2_Addition with wrong start_date
    body = {
        'start_date': 'wrong',
        'expire_date': '2025-12-29',
        'title': 'New year',
        'percent': 0.2,
        'description': 'Start new year by saving money',
        'usage_limitation': 10,
        'disposable': True,
        'one_use': True
    }

    response = client.post('/discounts', headers=header, json=body)

    assert response.status_code == 400

    # 3_Addition with wrong expire date
    body = {
        'start_date': '2025-01-01',
        'expire_date': 'wrong',
        'title': 'New year',
        'percent': 0.2,
        'description': 'Start new year by saving money',
        'usage_limitation': 10,
        'disposable': True,
        'one_use': True
    }

    response = client.post('/discounts', headers=header, json=body)

    assert response.status_code == 400

    # 4_Addition with long title
    body = {
        'start_date': '2025-01-01',
        'expire_date': '2025-12-29',
        'title': 'Nnnnnnnnnnnnnneeeeeeeeeewwwwwwwwwwwwwwwwwwwwwwww yyyyyyyeeeeeeeeeaaaaaaaaaaaarrrrrrrrrrrrrrrrrrrrr',
        'percent': 0.2,
        'description': 'Start new year by saving money',
        'usage_limitation': 10,
        'disposable': True,
        'one_use': True
    }

    response = client.post('/discounts', headers=header, json=body)

    assert response.status_code == 400

    # 5_Addition with wrong percent
    body = {
        'start_date': '2025-01-01',
        'expire_date': '2025-12-29',
        'title': 'New year',
        'percent': 20,
        'description': 'Start new year by saving money',
        'usage_limitation': 10,
        'disposable': True,
        'one_use': True
    }

    response = client.post('/discounts', headers=header, json=body)

    assert response.status_code == 400

    # 6_Addition with wrong usage_limitation
    body = {
        'start_date': '2025-01-01',
        'expire_date': '2025-12-29',
        'title': 'New year',
        'percent': 0.2,
        'description': 'Start new year by saving money',
        'usage_limitation': -6,
        'disposable': True,
        'one_use': True
    }

    response = client.post('/discounts', headers=header, json=body)

    assert response.status_code == 400

#    # 7_Addition with wrong disposable  # One of target: get type checking before fastapi and get 400 not 422
#    body = {
#        'start_date': '2025-01-01',
#        'expire_date': '2025-12-29',
#        'title': 'New year',
#        'percent': 0.2,
#        'description': 'Start new year by saving money',
#        'usage_limitation': 10,
#        'disposable': 'Wrong',
#        'one_use': True
#    }
#
#    response = client.post('/discounts', headers=header, json=body)
#
#    assert response.status_code == 400
#
#    # 8_Addition with wrong one use
#    body = {
#        'start_date': '2025-01-01',
#        'expire_date': '2025-12-29',
#        'title': 'New year',
#        'percent': 0.2,
#        'description': 'Start new year by saving money',
#        'usage_limitation': 10,
#        'disposable': True,
#        'one_use': 'Wrong'
#    }
#
#    response = client.post('/discounts', headers=header, json=body)
#
#    assert response.status_code == 400




def test_update_disposable():
    # 1_Update disposable successful to get 200
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjYsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiamoiLCJleHAiOjE3NzQ5MDU3OTd9.nhq20V7Ei7ifUsTK5zWflBGv2VFYv0IC2Ge1rD2xpGI'}
    body = {'disposable': False}

    response = client.put('/discounts/10', headers=header, json=body)

    assert response.status_code == 200

    # 2_Update disposable with wrong discount id
    response = client.put('/discounts/999', headers=header, json=body)

    assert response.status_code == 404

def test_get():
    # 1_Get a discount by id successful to get 200
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjYsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiamoiLCJleHAiOjE3NzQ5MDU3OTd9.nhq20V7Ei7ifUsTK5zWflBGv2VFYv0IC2Ge1rD2xpGI'}
    param = {'id': 10}

    response = client.get('/discounts', headers=header, params=param)

    assert response.status_code == 200

    # 2_Get all discounts
    response = client.get('/discounts', headers=header, params=param)

    assert response.status_code == 200

    # 3_Get all discounts by order_by
    param = {'order_by': ['id']}

    response = client.get('/discounts', headers=header, params=param)

    assert response.status_code == 200
