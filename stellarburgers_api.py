import allure
import requests
import urls



class StellarBurgersApi:

    @staticmethod
    def create_user(body):
        with allure.step('Создаём юзера'):
            return requests.post(urls.BASE_URL + urls.CREATE_USER, json=body)

    @staticmethod
    def auth_user(auth_body):
        with allure.step('Авторизуем юзера'):
            return requests.post(urls.BASE_URL + urls.AUTH_USER, json=auth_body)

    @staticmethod
    def changing_user(access, change_body):
        with allure.step('Изменяем данные юзера'):
            return requests.patch(urls.BASE_URL + urls.GET_AUTH_USER, headers={"Authorization": access}, json=change_body)

    @staticmethod
    def delete_user(access):
        with allure.step('Удаляем юзера'):
            return requests.delete(urls.BASE_URL + urls.GET_AUTH_USER, headers={"Authorization": access})

    @staticmethod
    def create_order(access, body_order):
        with allure.step('Создаём заказ'):
            return requests.post(urls.BASE_URL + urls.CREATE_AND_GET_ORDER, headers={"Authorization": access}, json=body_order)

    @staticmethod
    def get_ingredients():
        with allure.step('Получаем список ингредиентов'):
            return requests.get(urls.BASE_URL + urls.GET_INGREDIENTS)

    @staticmethod
    def get_order_certain_user(access):
        with allure.step('Получаем список заказов конкретного юзера'):
            return requests.get(urls.BASE_URL + urls.CREATE_AND_GET_ORDER, headers={"Authorization": access})
