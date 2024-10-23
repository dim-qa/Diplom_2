import requests
from samba.dcerpc.preg import header

import links
import pytest
import allure

class TestChangeUserData:

    @allure.story("User data")
    @allure.title("change name")
    def test_change_user_data_with_autorization(self, login_account, new_account):

        updated_user_data = {
            'name': login_account[1]
        }

        headers = {
            'Authorization': login_account[0],
            'Content-Type': 'application/json'
        }

        response = requests.patch(links.USER_DATA, headers=headers, json=updated_user_data)

        print(f"new name {response.json()['user']['name']}")
        assert response.json()['user']['name'] != login_account[2]

    @allure.story("User data")
    @allure.title("change mail")
    def test_change_user_data_with_autorization_change_mail(self, login_account, new_account):

        updated_user_data = {
            'name': login_account[3]
        }

        headers = {
            'Authorization': login_account[0],
            'Content-Type': 'application/json'
        }

        response = requests.patch(links.USER_DATA, headers=headers, json=updated_user_data)

        print(f"new email {response.json()['user']['email']}")
        assert response.status_code != 403

    @allure.story("User data")
    @allure.title("change data nonautorization")
    def test_change_user_data_with_nonautorization(self):
        updated_user_data = {
            'name': "New name"
        }

        headers = {
            'Authorization': 'token',
            'Content-Type': 'application/json'
        }

        response = requests.patch(links.USER_DATA, headers=headers, json=updated_user_data)

        assert response.status_code == 401

