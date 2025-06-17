from fastapi.testclient import TestClient

from restaurant.main import app


client = TestClient(app)


def test_addition():
    # 1_Create category successful to get 200
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTMsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiYmVobmFtX216IiwiZXhwIjoxNzc1MjUxMzQ1fQ.kbpdf6TYE4oqWnGxvDU3NVgq_Vx6KpOuHYUXRW6j8XY'}
    category = {'name': 'salam'}
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


def test_addition_item_to_category():
    header = {'admin-token-or-customer-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTMsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiYmVobmFtX216IiwiZXhwIjoxNzc1MjUxMzQ1fQ.kbpdf6TYE4oqWnGxvDU3NVgq_Vx6KpOuHYUXRW6j8XY'}
    param = {'order_by': ['id']}

    category = client.get('/categories', headers=header, params=param)

    category_id = eval(category.content.decode())['items'][-1]['id']

    # 1_Addition item to category successful to get 200
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTMsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiYmVobmFtX216IiwiZXhwIjoxNzc1MjUxMzQ1fQ.kbpdf6TYE4oqWnGxvDU3NVgq_Vx6KpOuHYUXRW6j8XY'}
    item = {'item_id': 3}

    response = client.post(f'/categories/{category_id}/items', json=item, headers=header)

    assert response.status_code == 200

    # 2_Addition item to not existed category
    response = client.post('/categories/400/items', json=item, headers=header)

    assert response.status_code == 404

    # 3_Addition not existed item to category
    not_existed_item = {'item_id': 400}

    response = client.post('/categories/41/items', json=not_existed_item, headers=header)

    assert response.status_code == 404

    # 4_Addition repeated item to category
    repeated_item = {'item_id': 3}

    response = client.post(f'/categories/{category_id}/items', json=repeated_item, headers=header)

    assert response.status_code == 409


def test_delete_item_from_category():
    header = {'admin-token-or-customer-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTMsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiYmVobmFtX216IiwiZXhwIjoxNzc1MjUxMzQ1fQ.kbpdf6TYE4oqWnGxvDU3NVgq_Vx6KpOuHYUXRW6j8XY'}
    param = {'order_by': ['id']}

    category = client.get('/categories', headers=header, params=param)

    category_id = eval(category.content.decode())['items'][-1]['id']

    # 1_Delete item from category successful to get 200
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTMsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiYmVobmFtX216IiwiZXhwIjoxNzc1MjUxMzQ1fQ.kbpdf6TYE4oqWnGxvDU3NVgq_Vx6KpOuHYUXRW6j8XY'}

    response = client.delete(f'/categories/{category_id}/items/3', headers=header)

    assert response.status_code == 200

    # 2_Delete item from not existed category
    response = client.delete('/categories/999/items/4', headers=header)

    assert response.status_code == 404

    # 3_Delete not existed item from category
    response = client.delete('/categories/40/items/999', headers=header)

    assert response.status_code == 404

    # 4_Delete item that is just in one category
    response = client.delete('/categories/62/items/3', headers=header)

    assert response.status_code == 400

    # 5_Delete item that is not in category
    response = client.delete(f'/categories/{category_id}/items/4', headers=header)

    assert response.status_code == 404



def test_get_items_in_category():
    header = {'admin-token-or-customer-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTMsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiYmVobmFtX216IiwiZXhwIjoxNzc1MjUxMzQ1fQ.kbpdf6TYE4oqWnGxvDU3NVgq_Vx6KpOuHYUXRW6j8XY'}
    param = {'order_by': ['id']}

    category = client.get('/categories', headers=header, params=param)

    category_id = eval(category.content.decode())['items'][-1]['id']

    # 1_Get items from category successful to get 200
    header = {'admin-token-or-customer-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTMsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiYmVobmFtX216IiwiZXhwIjoxNzc1MjUxMzQ1fQ.kbpdf6TYE4oqWnGxvDU3NVgq_Vx6KpOuHYUXRW6j8XY'}

    response = client.get(f'/categories/{category_id}/items', headers=header)

    assert response.status_code == 200

    # 2_Get items from not existed category
    response = client.get('/categories/999/items', headers=header)

    assert response.status_code == 404

    # 3_Get items from category with order_by
    param = {'order_by': ['id']}

    response = client.get(f'/categories/{category_id}/items', headers=header, params=param)

    assert response.status_code == 200

    # 4_Get items from category with wrong order_by
    param = {'order_by': ['Somthing that is not in item rows']}

    response = client.get('/categories/41/items', headers=header, params=param)

    assert response.status_code == 400


def test_delete_category():
    header = {'admin-token-or-customer-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTMsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiYmVobmFtX216IiwiZXhwIjoxNzc1MjUxMzQ1fQ.kbpdf6TYE4oqWnGxvDU3NVgq_Vx6KpOuHYUXRW6j8XY'}
    param = {'order_by': ['id']}

    category = client.get('/categories', headers=header)

    category_id = eval(category.content.decode())['items'][-1]['id']
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', category_id)

    # 1_Delete item successful to get 200
    header = {'admin-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTMsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoiYmVobmFtX216IiwiZXhwIjoxNzc1MjUxMzQ1fQ.kbpdf6TYE4oqWnGxvDU3NVgq_Vx6KpOuHYUXRW6j8XY'}

    response = client.delete(f'/categories/{category_id}', headers=header)

    assert response.status_code == 200

    # 2_Delete a category that has item
    response = client.delete(f'/categories/62', headers=header)

    assert response.status_code == 400

    # 3_Delete a not existed category
    response = client.delete('/categories/999', headers=header)

    assert response.status_code == 404

