import requests


def test_simple_req():
    resp = requests.get('http://5.101.50.27:8000/company/list')
    response_body = resp.json()
    first_company = response_body[0]
    assert first_company['name'] == "QA Студия 'ТестировщикЪ'"
    assert resp.status_code == 200
    assert resp.headers["content-type"] == 'application/json'


def test_auth():
    data = {
        "username": 'harrypotter',
        "password": 'expelliarmus'}
    resp = requests.post('http://5.101.50.27:8000/auth/login', json=data)
    assert resp.status_code == 200


def test_create_new_company():
    auth_data = {
        "username": 'harrypotter',
        "password": 'expelliarmus'
    }

    resp = requests.post('http://5.101.50.27:8000/auth/login', json=auth_data)
    token = resp.json()["user_token"]
    headers = {"x-client-token": token}

    company = {
        "name": "Velo",
        "description": "the  best",
        "is_active": True
    }

    resp = requests.post('http://5.101.50.27:8000/company/create', json=company, headers=headers)
    assert resp.status_code == 201
