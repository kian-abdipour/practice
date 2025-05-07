from fastapi.testclient import TestClient

from restaurant.main import app


client = TestClient(app)


def test_addition():
    # 1_Create category successful to get 200
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTMsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiYmVobmFtX216IiwiZXhwIjoxNzc1MjUxMzQ1fQ.kbpdf6TYE4oqWnGxvDU3NVgq_Vx6KpOuHYUXRW6j8XY'}
    category = {'name': 'fastfood'}
    response = client.post('/categories', json=category, headers=header)

    assert response.status_code == 200

    # 2_Create category with repeated name
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTMsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiYmVobmFtX216IiwiZXhwIjoxNzc1MjUxMzQ1fQ.kbpdf6TYE4oqWnGxvDU3NVgq_Vx6KpOuHYUXRW6j8XY'}
    category = {'name': 'fastfood'}
    response = client.post('/categories', json=category, headers=header)

    assert response.status_code == 409

    # 3_Create category with long name
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTMsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiYmVobmFtX216IiwiZXhwIjoxNzc1MjUxMzQ1fQ.kbpdf6TYE4oqWnGxvDU3NVgq_Vx6KpOuHYUXRW6j8XY'}
    category = {'name': 'faaaaaaaaaaaaaaaaaaaaaaaaaaaaassssssssssssssssssssssssssstttttttttttttttttfoodddddddddddddddd'}
    response = client.post('/categories', json=category, headers=header)

    assert response.status_code == 400


def test_get():
    # 1_Get successful to get 200
    header = {'admin-token-or-customer-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTMsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiYmVobmFtX216IiwiZXhwIjoxNzc1MjUxMzQ1fQ.kbpdf6TYE4oqWnGxvDU3NVgq_Vx6KpOuHYUXRW6j8XY'}
    all_categories_response = client.get('/categories', headers=header)

    assert all_categories_response.status_code == 200

    all_categories = eval(all_categories_response.content.decode())['items']

    # 2_Get a category by id
    category_id = all_categories[0]['id']
    category = {'id': category_id}
    response = client.get('/categories', params=category, headers=header)

    assert response.status_code == 200

    # 3_Get a category by name
    category_name = all_categories[0]['name']
    category = {'name': category_name}
    response = client.get('/categories', params=category, headers=header)

    assert response.status_code == 200

    # 4_Get all categories by order by
    category = {'order_by': ['id']}
    response = client.get('/categories', params=category, headers=header)

    assert response.status_code == 200

    # 5_Get a category with wrong id
    category = {'id': 85}
    response = client.get('/categories', params=category, headers=header)

    assert response.status_code == 404

    # 6_Get a category with wrong username
    category = {'name': 'Wrong username'}
    response = client.get('/categories', params=category, headers=header)

    assert response.status_code == 404

    # 7_Get all categories by wrong order_by
    category = {'order_by': ['Somthing that is not in category attribute']}
    response = client.get('/categories', params=category, headers=header)

    assert response.status_code == 400

