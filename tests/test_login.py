import requests
import links
import pytest
import allure


class TestLogin:

    @allure.story("User Login")
    @allure.title("Successful User Login")
    def test_login_by_an_existing_user(self, ready_account):
        response = requests.post(links.LOGIN, json={
            "email": f'{ready_account["email"]}',
            "password": f'{ready_account["password"]}',
            "name": f'{ready_account["name"]}'
        })
        assert response.status_code == 200

    @allure.story("User Login")
    @allure.title("Unsuccessful User Login")
    def test_login_by_an_non_existing_user(self):
        response = requests.post(links.LOGIN, json={
            "email": 'account@account.account',
            "password": 'account',
            "name": 'account'
        })
        assert response.status_code == 401
