from fastapi.testclient import TestClient

from restaurant.main import app


client = TestClient(app)


def test_addition():
    # 1_Addition address successful to get 200
    address = {'address': 'Heravi, zabeti, sharifi gharby, pelak 40'}
    header = {'customer-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUsInJvbGUiOiJjdXN0b21lciIsInVzZXJuYW1lIjoibWF0aW4iLCJleHAiOjE3NzUxNjU3NTZ9.fu6HdZ_wKF6EYWfHm704rd831mKO8fjIWykFi_Nc85c'}
    response = client.post('/addresses', json=address, headers=header)

    assert response.status_code == 200

    # 2_Addition address with long len
    address = {'address': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'}
    header = {'customer-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUsInJvbGUiOiJjdXN0b21lciIsInVzZXJuYW1lIjoibWF0aW4iLCJleHAiOjE3NzUxNjU3NTZ9.fu6HdZ_wKF6EYWfHm704rd831mKO8fjIWykFi_Nc85c'}
    response = client.post('/addresses', json=address, headers=header)

    assert response.status_code == 400


def test_get():
    # 1_Get all address successful
    header = {'customer-or-admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUsInJvbGUiOiJjdXN0b21lciIsInVzZXJuYW1lIjoibWF0aW4iLCJleHAiOjE3NzUxNjU3NTZ9.fu6HdZ_wKF6EYWfHm704rd831mKO8fjIWykFi_Nc85c'}
    response = client.get('/addresses', headers=header)

    assert response.status_code == 200

    # 2_Get address by id
    address_id = eval(client.get('/addresses', headers=header).content.decode())['items'][0]['id']
    address = {'id': address_id}
    header = {'customer-or-admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUsInJvbGUiOiJjdXN0b21lciIsInVzZXJuYW1lIjoibWF0aW4iLCJleHAiOjE3NzUxNjU3NTZ9.fu6HdZ_wKF6EYWfHm704rd831mKO8fjIWykFi_Nc85c'}
    response = client.get('/addresses', params=address, headers=header)

    assert response.status_code == 200

    # 3_Get all address with order_by
    address = {'order_by': ['id']}
    header = {'customer-or-admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUsInJvbGUiOiJjdXN0b21lciIsInVzZXJuYW1lIjoibWF0aW4iLCJleHAiOjE3NzUxNjU3NTZ9.fu6HdZ_wKF6EYWfHm704rd831mKO8fjIWykFi_Nc85c'}
    response = client.get('/addresses', params=address, headers=header)

    assert response.status_code == 200

    # 4_Get with wrong id
    address = {'id': 99}
    header = {'customer-or-admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUsInJvbGUiOiJjdXN0b21lciIsInVzZXJuYW1lIjoibWF0aW4iLCJleHAiOjE3NzUxNjU3NTZ9.fu6HdZ_wKF6EYWfHm704rd831mKO8fjIWykFi_Nc85c'}
    response = client.get('/addresses', params=address, headers=header)

    assert response.status_code == 404

    # 5_Get with wrong order_by
    address = {'order_by': ['Somting that is not in address rows']}
    header = {'customer-or-admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUsInJvbGUiOiJjdXN0b21lciIsInVzZXJuYW1lIjoibWF0aW4iLCJleHAiOjE3NzUxNjU3NTZ9.fu6HdZ_wKF6EYWfHm704rd831mKO8fjIWykFi_Nc85c'}
    response = client.get('/addresses', params=address, headers=header)

    assert response.status_code == 400


def test_delete():
    # 1_Delete an address successful
    header = {'customer-or-admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUsInJvbGUiOiJjdXN0b21lciIsInVzZXJuYW1lIjoibWF0aW4iLCJleHAiOjE3NzUxNjU3NTZ9.fu6HdZ_wKF6EYWfHm704rd831mKO8fjIWykFi_Nc85c'}
    address_id = eval(client.get('/addresses', headers=header).content.decode())['items'][-1]['id']

    header = {'customer-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUsInJvbGUiOiJjdXN0b21lciIsInVzZXJuYW1lIjoibWF0aW4iLCJleHAiOjE3NzUxNjU3NTZ9.fu6HdZ_wKF6EYWfHm704rd831mKO8fjIWykFi_Nc85c'}
    response = client.delete(f'/addresses/{address_id}', headers=header)

    assert response.status_code == 200

    # 2_Delete with wrong id
    header = {'customer-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUsInJvbGUiOiJjdXN0b21lciIsInVzZXJuYW1lIjoibWF0aW4iLCJleHAiOjE3NzUxNjU3NTZ9.fu6HdZ_wKF6EYWfHm704rd831mKO8fjIWykFi_Nc85c'}
    response = client.delete('/addresses/99', headers=header)

    assert response.status_code == 404




