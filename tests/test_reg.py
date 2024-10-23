import requests
import links
import pytest
import allure


class TestAccount:

    @allure.story("User Registration")
    @allure.title("Successful User Registration")
    def test_register_user_success(self, new_account):
        response = requests.post(links.REGISTER_USER_URL, json={
        "email": f'{new_account[0]}',
        "password": f'{new_account[1]}',
        "name": f'{new_account[2]}'
    })
        assert response.status_code == 200

    @allure.story("User Registration")
    @allure.title("User Already Exists")
    def test_register_user_already_exists(self, new_account):
        requests.post(links.REGISTER_USER_URL, json={
        "email": f'{new_account[0]}',
        "password": f'{new_account[1]}',
        "name": f'{new_account[2]}'
    })
        response = requests.post(links.REGISTER_USER_URL, json={
        "email": f'{new_account[0]}',
        "password": f'{new_account[1]}',
        "name": f'{new_account[2]}'
    })
        assert response.status_code == 403

    @allure.story("User Registration")
    @allure.title("Missing Email Field")
    def test_register_user_missing_fields_mail(self, new_account):
        response = requests.post(links.REGISTER_USER_URL, json={
        "password": f'{new_account[1]}',
        "name": f'{new_account[2]}'
    })
        assert response.status_code == 403

    @allure.story("User Registration")
    @allure.title("Missing Password Field")
    def test_register_user_missing_fields_password(self, new_account):
        response = requests.post(links.REGISTER_USER_URL, json={
        "email": f'{new_account[0]}',
        "name": f'{new_account[2]}'
    })
        assert response.status_code == 403

    @allure.story("User Registration")
    @allure.title("Missing Username Field")
    def test_register_user_missing_fields_username(self, new_account):
        response = requests.post(links.REGISTER_USER_URL, json={
        "email": f'{new_account[0]}',
        "password": f'{new_account[1]}'
    })
        assert response.status_code == 403
