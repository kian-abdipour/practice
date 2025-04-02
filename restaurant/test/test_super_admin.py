from fastapi.testclient import TestClient

from restaurant.main import app


client = TestClient(app)


def test_login():
    # 1_Login successful to get 200
    super_admin = {'username': 'Kian_Abdipour', 'password': 'kK86!@Kk'}
    response = client.post('/super-admin-tokens', json=super_admin)

    assert response.status_code == 200

    # 2_Login with wrong username
    super_admin = {'username': 'wrong username', 'password': 'kK86!@Kk'}
    response = client.post('/super-admin-tokens', json=super_admin)

    assert response.status_code == 401

    # 3_Login with wrong password
    super_admin = {'username': 'Kian_Abdipour', 'password': 'kK86!@KK'}
    response = client.post('/super-admin-tokens', json=super_admin)

    assert response.status_code == 401

    # 4_Login with long username
    super_admin = {'username': 'loooooooong usernameeeeeeeeeeeeeeeeeee', 'password': 'kK86!@Kk'}
    response = client.post('/super-admin-tokens', json=super_admin)

    assert response.status_code == 400

    # 5_Login with short username
    super_admin = {'username': 'Ki', 'password': 'kK86!@Kk'}
    response = client.post('/super-admin-tokens', json=super_admin)

    assert response.status_code == 400

    # 6_Login with password that it's len is not 8 and has wrong pattern
    super_admin = {'username': 'Kian_Abdipour', 'password': 'passssworrrdddd'}
    response = client.post('/super-admin-tokens', json=super_admin)

    assert response.status_code == 400


