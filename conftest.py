import random
import string

import pytest
import requests

import links


@pytest.fixture
def new_account():
    letters = string.ascii_lowercase  # Используем только строчные буквы
    email = ''.join(random.choice(letters) for _ in range(8))
    password = ''.join(random.choice(letters) for _ in range(8))
    name = ''.join(random.choice(letters) for _ in range(8))
    return [f'{email}@test.ru', password, name]

@pytest.fixture
def ready_account(new_account):
    response = requests.post(links.REGISTER_USER_URL, json={
        "email": f'{new_account[0]}',
        "password": f'{new_account[1]}',
        "name": f'{new_account[2]}'
    })
    return {'email': response.json()['user']['email'],
            'name': response.json()['user']['name'],
            'password': new_account[1],
            'accessToken': response.json()['accessToken']
            }

@pytest.fixture
def login_account(ready_account):
    headers = {
        'Authorization': ready_account['accessToken'],
        'Content-Type': 'application/json'
    }
    response = requests.get(links.USER_DATA, headers=headers)
    print(f"was name is {response.json()['user']['name']} and was email {response.json()['user']['email']}")
    return [ready_account['accessToken'], f"{''.join(random.choice(string.ascii_lowercase) for _ in range(8))}@yandex.ru", response.json()['user']['name'], response.json()['user']['email']]

@pytest.fixture
def get_ingredients():
    response = requests.get(links.INGREDIENTS)
    return [response.json()['data'][1]['_id'], response.json()['data'][2]['_id']]

