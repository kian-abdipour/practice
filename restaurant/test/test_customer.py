from fastapi.testclient import TestClient

from restaurant.main import app

client = TestClient(app)


def test_signup():
    # 1_Signup successful to get 200
    customer = {'username': 'matin_gh', 'password': 'kK86!@Kk', 'phone_number': '09100739361'}
    response = client.post('/customer-registrations', json=customer)

    assert response.status_code == 200

    # 2_Signup with long username
    customer = {'username': 'matinnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn', 'password': 'kK86!@Kk', 'phone_number': '09100739361'}
    response = client.post('/customer-registrations', json=customer)

    assert response.status_code == 400

    # 3_Signup with short username
    customer = {'username': 'm', 'password': 'kK86!@Kk', 'phone_number': '09100739361'}
    response = client.post('/customer-registrations', json=customer)

    assert response.status_code == 400

    # 4_Signup with wrong password pattern
    customer = {'username': 'matin', 'password': 'asdf', 'phone_number': '09100739361'}
    response = client.post('/customer-registrations', json=customer)

    assert response.status_code == 400

    # 5_Signup with wrong phone_number pattern
    customer = {'username': 'matin', 'password': 'kK86!@Kk', 'phone_number': '09100739360000000000000000000000'}
    response = client.post('/customer-registrations', json=customer)

    assert response.status_code == 400

    # 6_Signup with username that already exist
    customer = {'username': 'matin', 'password': 'kK86!@Kk', 'phone_number': '09100739361'}
    response = client.post('/customer-registrations', json=customer)

    assert response.status_code == 409

    # 7_Signup with phone_number that already exist
    customer = {'username': 'kian', 'password': 'kK86!@Kk', 'phone_number': '09100739361'}
    response = client.post('/customer-registrations', json=customer)

    assert response.status_code == 409


def test_login():
    # 1_Login successful to get 200
    customer = {'username': 'matin_gh', 'password': 'kK86!@Kk'}
    response = client.post('/customer-tokens', json=customer)

    assert response.status_code == 200

    # 2_Login with wrong username
    customer = {'username': 'wrong username', 'password': 'kK86!@Kk'}
    response = client.post('/customer-tokens', json=customer)

    assert response.status_code == 401

    # 3_Login with wrong password
    customer = {'username': 'matin_gh', 'password': 'aK86!@Kk'}
    response = client.post('/customer-tokens', json=customer)

    assert response.status_code == 401


def test_get():
    # 1_Get with username successful
    customer = {'username': 'matin_gh'}
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjYsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiamoiLCJleHAiOjE3NzQ5MDU3OTd9.nhq20V7Ei7ifUsTK5zWflBGv2VFYv0IC2Ge1rD2xpGI'}
    response = client.get('/customers', params=customer, headers=header)

    assert response.status_code == 200

    # 2_Get with id successful
    customer_id = eval(response.content.decode())['id']
    customer = {'id': customer_id}
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjYsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiamoiLCJleHAiOjE3NzQ5MDU3OTd9.nhq20V7Ei7ifUsTK5zWflBGv2VFYv0IC2Ge1rD2xpGI'}
    response = client.get('/customers', params=customer, headers=header)

    assert response.status_code == 200

    # 3_Get with phone_number successful
    customer = {'phone_number': '09100739361'}
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjYsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiamoiLCJleHAiOjE3NzQ5MDU3OTd9.nhq20V7Ei7ifUsTK5zWflBGv2VFYv0IC2Ge1rD2xpGI'}
    response = client.get('/customers', params=customer, headers=header)

    assert response.status_code == 200

    # 4_Get all customer
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjYsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiamoiLCJleHAiOjE3NzQ5MDU3OTd9.nhq20V7Ei7ifUsTK5zWflBGv2VFYv0IC2Ge1rD2xpGI'}
    response = client.get('/customers', headers=header)

    assert response.status_code == 200

    # 5_Get all with order_by
    customer = {'order_by': ['id']}
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjYsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiamoiLCJleHAiOjE3NzQ5MDU3OTd9.nhq20V7Ei7ifUsTK5zWflBGv2VFYv0IC2Ge1rD2xpGI'}
    response = client.get('/customers', params=customer, headers=header)

    assert response.status_code == 200

    # 6_Get with wrong id
    customer = {'id': 1}
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjYsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiamoiLCJleHAiOjE3NzQ5MDU3OTd9.nhq20V7Ei7ifUsTK5zWflBGv2VFYv0IC2Ge1rD2xpGI'}
    response = client.get('/customers', params=customer, headers=header)

    assert response.status_code == 404

    # 7_Get with wrong username
    customer = {'username': 'wrong username'}
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjYsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiamoiLCJleHAiOjE3NzQ5MDU3OTd9.nhq20V7Ei7ifUsTK5zWflBGv2VFYv0IC2Ge1rD2xpGI'}
    response = client.get('/customers', params=customer, headers=header)

    assert response.status_code == 404

    # 8_Get with wrong phone_number
    customer = {'phone_number': '09100739369'}
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjYsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiamoiLCJleHAiOjE3NzQ5MDU3OTd9.nhq20V7Ei7ifUsTK5zWflBGv2VFYv0IC2Ge1rD2xpGI'}
    response = client.get('/customers', params=customer, headers=header)

    assert response.status_code == 404

    # 9_Get with wrong order_by
    customer = {'order_by': ['somthing that is not in customer rows']}
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjYsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiamoiLCJleHAiOjE3NzQ5MDU3OTd9.nhq20V7Ei7ifUsTK5zWflBGv2VFYv0IC2Ge1rD2xpGI'}
    response = client.get('/customers', params=customer, headers=header)

    assert response.status_code == 400


