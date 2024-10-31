import requests
import links
import pytest
import allure

class TestOrder:

    @allure.story("Create order")
    @allure.title("create order with_auth")
    def test_create_order_with_auth(self, login_account, get_ingredients):
        token = login_account[1]
        headers = {"Authorization": f"{token}"}
        response = requests.post(links.ORDER,
                                 json={"ingredients": [f"{get_ingredients[1]}"]},
                                 headers=headers)
        assert response.status_code == 200

    @allure.story("Create order")
    @allure.title("create order without auth")
    def test_create_order_without_auth(self, get_ingredients):
        response = requests.post(links.ORDER, json={"ingredients": [f"{get_ingredients[1]}"]})
        assert response.status_code == 200

    @allure.story("Create order")
    @allure.title("create order with ingredients")
    def test_create_order_with_ingredients(self, get_ingredients):
        response = requests.post(links.ORDER, json={"ingredients": [f"{get_ingredients[0]}", f"{get_ingredients[1]}"]})
        assert response.status_code == 200

    @allure.story("Create order")
    @allure.title("create order without ingredients")
    def test_create_order_without_ingredients(self):
        response = requests.post(links.ORDER, json={})
        assert response.status_code == 400

    @allure.story("Create order")
    @allure.title("create order with invalid ingredient")
    def test_create_order_with_invalid_ingredient(self):
        response = requests.post(links.ORDER, json={"ingredients": ['ingredient']})
        assert response.status_code == 500