from fastapi.testclient import TestClient

from restaurant.main import app


client = TestClient(app)


def test_addition():
    # 1_Addition by not existed discount
    header = {'customer-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUsInJvbGUiOiJjdXN0b21lciIsInVzZXJuYW1lIjoibWF0aW4iLCJleHAiOjE3NzUxNjU3NTZ9.fu6HdZ_wKF6EYWfHm704rd831mKO8fjIWykFi_Nc85c'}
    body = {
        'delivery_type': 'Bike delivery',
        'desk_number': 10,
        'description': '',
        'payment_type': 'Online',
        'discount_code': 'arK131121?',
        'address_id': 9
    }

    response = client.post('/orders', headers=header, json=body)

    assert response.status_code == 404

    # 2_Addition by not available discount
    body = {
        'delivery_type': 'Bike delivery',
        'desk_number': 10,
        'description': '',
        'payment_type': 'Online',
        'discount_code': 'QGi723112!',
        'address_id': 9
    }

    response = client.post('/orders', headers=header, json=body)

    assert response.status_code == 400

    # 3_Addition by discount that is not started
    body = {
        'delivery_type': 'Bike delivery',
        'desk_number': 10,
        'description': '',
        'payment_type': 'Online',
        'discount_code': 'kCA598105#',
        'address_id': 9
    }

    response = client.post('/orders', headers=header, json=body)

    assert response.status_code == 400

    #4_Addition by discount that is expired
    body = {
        'delivery_type': 'Bike delivery',
        'desk_number': 10,
        'description': '',
        'payment_type': 'Online',
        'discount_code': 'KRF150113.',
        'address_id': 9
    }

    response = client.post('/orders', headers=header, json=body)

    assert response.status_code == 400

    #5_Addition by discount that is out of stock
    body = {
        'delivery_type': 'Bike delivery',
        'desk_number': 10,
        'description': '',
        'payment_type': 'Online',
        'discount_code': 'YPX703112$',
        'address_id': 9
    }

    response = client.post('/orders', headers=header, json=body)

    assert response.status_code == 400



#    # 2_Addition successful to get 200
#    body = {
#        'delivery_type': 'Bike delivery',
#        'desk_number': 10,
#        'description': '',
#        'payment_type': 'Online',
#        'discount_code': 'urK131121?',
#        'address_id': 9
#    }
#
#    response = client.post('/orders', headers=header, json=body)
#
#    assert response.status_code == 200
#
#    # 3_Addition by used discount
#    body = {
#        'delivery_type': 'Bike delivery',
#        'desk_number': 10,
#        'description': '',
#        'payment_type': 'Online',
#        'discount_code': 'urK131121?',
#        'address_id': 9
#    }
#
#    response = client.post('/orders', headers=header, json=body)
#
#    assert response.status_code == 400
#
#    # 4_Addition an order with empty cart
#    response = client.post('/orders', headers=header, json=body)
#
#    assert response.status_code == 400
#
#