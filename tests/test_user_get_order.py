import requests
import links
import pytest
import allure

class TestGetOrder:

    @allure.story("Get user order")
    @allure.title("get orders authorized user")
    def test_get_orders_authorized_user(self, login_account):
        token = login_account[0]  # Замените на ваш токен
        headers = {"Authorization": token}
        response = requests.get(links.GET_ORDER, headers=headers)
        assert response.status_code == 200

    @allure.story("Get user order")
    @allure.title("get orders unauthorized user")
    def test_get_orders_unauthorized_user(self):
        response = requests.get(links.GET_ORDER, headers=None)
        assert response.status_code, 401
