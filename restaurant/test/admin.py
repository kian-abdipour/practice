from fastapi.testclient import TestClient
from restaurant.main import app

client = TestClient(app)


def test_addition():
    # 1_Addition successful to get 200
    admin = {'first_name': 'Nima', 'last_name': 'Judy', 'username': 'jj', 'password': 'kK86!@Kk'}
    header = {'super-admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwicm9sZSI6InN1cGVyX2FkbWluIiwidXNlcm5hbWUiOiJLaWFuX0FiZGlwb3VyIiwiZXhwIjoxNzc0ODE3MDU3fQ.sTi3zNOa4R-ZHDWdRhyOHIA4rbLd-IqveOUU7-Y_75U'}
    responses = client.post('/admins', json=admin, headers=header)

    assert responses.status_code == 200

    # 2_Addition with short firstname
    admin = {'first_name': 'Ni', 'last_name': 'Judy', 'username': 'jj', 'password': 'kK86!@Kk'}
    responses = client.post('/admins', json=admin, headers=header)

    assert responses.status_code == 400

    # 3_Addition with long firstname
    admin = {'first_name': 'Niiiiiiiiiiiiiiiiiiiiiiimma', 'last_name': 'Judy', 'username': 'jj', 'password': 'kK86!@Kk'}
    responses = client.post('/admins', json=admin, headers=header)

    assert responses.status_code == 400

    # 4_Addition with short last_name
    admin = {'first_name': 'Nima', 'last_name': 'Ju', 'username': 'jj', 'password': 'kK86!@Kk'}
    header = {'super-admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwicm9sZSI6InN1cGVyX2FkbWluIiwidXNlcm5hbWUiOiJLaWFuX0FiZGlwb3VyIiwiZXhwIjoxNzc0ODE3MDU3fQ.sTi3zNOa4R-ZHDWdRhyOHIA4rbLd-IqveOUU7-Y_75U'}
    responses = client.post('/admins', json=admin, headers=header)

    assert responses.status_code == 400

    # 5_Addition with long last_name
    admin = {'first_name': 'Nima', 'last_name': 'Judyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy', 'username': 'jj', 'password': 'kK86!@Kk'}
    responses = client.post('/admins', json=admin, headers=header)

    assert responses.status_code == 400

    # 6_Addition with short username
    admin = {'first_name': 'Nima', 'last_name': 'Judy', 'username': 'j', 'password': 'kK86!@Kk'}
    header = {'super-admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwicm9sZSI6InN1cGVyX2FkbWluIiwidXNlcm5hbWUiOiJLaWFuX0FiZGlwb3VyIiwiZXhwIjoxNzc0ODE3MDU3fQ.sTi3zNOa4R-ZHDWdRhyOHIA4rbLd-IqveOUU7-Y_75U'}
    responses = client.post('/admins', json=admin, headers=header)

    assert responses.status_code == 400

    # 7_Addition with long username
    admin = {'first_name': 'Nima', 'last_name': 'Judy', 'username': 'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj', 'password': 'kK86!@Kk'}
    header = {'super-admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwicm9sZSI6InN1cGVyX2FkbWluIiwidXNlcm5hbWUiOiJLaWFuX0FiZGlwb3VyIiwiZXhwIjoxNzc0ODE3MDU3fQ.sTi3zNOa4R-ZHDWdRhyOHIA4rbLd-IqveOUU7-Y_75U'}
    responses = client.post('/admins', json=admin, headers=header)

    assert responses.status_code == 400

    # 8_Addition with password that len it's not 8
    admin = {'first_name': 'Nima', 'last_name': 'Judy', 'username': 'jj', 'password': 'kK86!@Kkkkkkkk'}
    header = {'super-admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwicm9sZSI6InN1cGVyX2FkbWluIiwidXNlcm5hbWUiOiJLaWFuX0FiZGlwb3VyIiwiZXhwIjoxNzc0ODE3MDU3fQ.sTi3zNOa4R-ZHDWdRhyOHIA4rbLd-IqveOUU7-Y_75U'}
    responses = client.post('/admins', json=admin, headers=header)

    assert responses.status_code == 400


def test_login():
    # 1_Login successful to get 200
    admin = {'username': 'jj', 'password': 'kK86!@Kk'}
    responses = client.post('/admin-tokens', json=admin)

    assert responses.status_code == 200

    # 2_Login with wrong username
    admin = {'username': 'wrong username', 'password': 'kK86!@Kk'}
    responses = client.post('/admin-tokens', json=admin)

    assert responses.status_code == 401

    # 3_Login with wrong password
    admin = {'username': 'jj', 'password': 'kK86!@Kw'}
    responses = client.post('/admin-tokens', json=admin)

    assert responses.status_code == 401

    # 4_Login with long username
    admin = {'username': 'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj', 'password': 'kK86!@Kk'}
    responses = client.post('/admin-tokens', json=admin)

    assert responses.status_code == 400

    # 5_Login with short username
    admin = {'username': 'j', 'password': 'kK86!@Kk'}
    responses = client.post('/admin-tokens', json=admin)

    assert responses.status_code == 400

    # 6_Login with password that it's len is not 8 and hase wrong pattern
    admin = {'username': 'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj', 'password': 'kK86!@Kk'}
    responses = client.post('/admin-tokens', json=admin)

    assert responses.status_code == 400


def test_get():
    # 1_Get an admin successful
    admin = {'id': 24}
    header = {'super-admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwicm9sZSI6InN1cGVyX2FkbWluIiwidXNlcm5hbWUiOiJLaWFuX0FiZGlwb3VyIiwiZXhwIjoxNzc0ODE3MDU3fQ.sTi3zNOa4R-ZHDWdRhyOHIA4rbLd-IqveOUU7-Y_75U'}
    responses = client.get('/admins', params=admin, headers=header)

    assert responses.status_code == 200

    # 2_Get all admins successful
    header = {'super-admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwicm9sZSI6InN1cGVyX2FkbWluIiwidXNlcm5hbWUiOiJLaWFuX0FiZGlwb3VyIiwiZXhwIjoxNzc0ODE3MDU3fQ.sTi3zNOa4R-ZHDWdRhyOHIA4rbLd-IqveOUU7-Y_75U'}
    responses = client.get('/admins', headers=header)

    assert responses.status_code == 200

    # 3_Get all admin by order_by
    admin = {'order_by': ['id']}
    header = {'super-admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwicm9sZSI6InN1cGVyX2FkbWluIiwidXNlcm5hbWUiOiJLaWFuX0FiZGlwb3VyIiwiZXhwIjoxNzc0ODE3MDU3fQ.sTi3zNOa4R-ZHDWdRhyOHIA4rbLd-IqveOUU7-Y_75U'}
    responses = client.get('/admins', headers=header, params=admin)

    assert responses.status_code == 200

    # 4_Get with wrong id
    admin = {'id': 1}
    header = {'super-admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwicm9sZSI6InN1cGVyX2FkbWluIiwidXNlcm5hbWUiOiJLaWFuX0FiZGlwb3VyIiwiZXhwIjoxNzc0ODE3MDU3fQ.sTi3zNOa4R-ZHDWdRhyOHIA4rbLd-IqveOUU7-Y_75U'}
    responses = client.get('/admins', params=admin, headers=header)

    assert responses.status_code == 404

    # 5_Get with wrong order_by
    admin = {'order_by': ['somthing that is not in admin rows']}
    header = {'super-admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwicm9sZSI6InN1cGVyX2FkbWluIiwidXNlcm5hbWUiOiJLaWFuX0FiZGlwb3VyIiwiZXhwIjoxNzc0ODE3MDU3fQ.sTi3zNOa4R-ZHDWdRhyOHIA4rbLd-IqveOUU7-Y_75U'}
    responses = client.get('/admins', headers=header, params=admin)

    assert responses.status_code == 400


def test_delete():
    # 1_Delete admin successful
#    admin = {'id': 24}
    header = {'super-admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwicm9sZSI6InN1cGVyX2FkbWluIiwidXNlcm5hbWUiOiJLaWFuX0FiZGlwb3VyIiwiZXhwIjoxNzc0ODE3MDU3fQ.sTi3zNOa4R-ZHDWdRhyOHIA4rbLd-IqveOUU7-Y_75U'}
    responses = client.delete('/admins/24', headers=header)

    assert responses.status_code == 200

    # 2_Delete admin with wrong password
    #    admin = {'id': 24}
    header = {
        'super-admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwicm9sZSI6InN1cGVyX2FkbWluIiwidXNlcm5hbWUiOiJLaWFuX0FiZGlwb3VyIiwiZXhwIjoxNzc0ODE3MDU3fQ.sTi3zNOa4R-ZHDWdRhyOHIA4rbLd-IqveOUU7-Y_75U'}
    responses = client.delete('/admins/2', headers=header)

    assert responses.status_code == 404

