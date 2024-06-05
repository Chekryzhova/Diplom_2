from stellarburgers_api import StellarBurgersApi
import data
import allure


class TestGetOrderList:

    @allure.title('Проверка получения заказов пользователя с авторизацией')
    @allure.description('Создаём пользователя, авторизуемся им и получаем список его заказов. После проверки удаляем пользователя')
    def test_get_order_list_certain_user_with_authorization(self):
        StellarBurgersApi.create_user(data.CREATE_USER_BODY)
        auth_body = {
            "email": data.CREATE_USER_BODY["email"],
            "password": data.CREATE_USER_BODY["password"]
        }
        auth_user_requests = StellarBurgersApi.auth_user(auth_body)
        access = auth_user_requests.json()["accessToken"]
        get_order_requests = StellarBurgersApi.get_order_certain_user(access)

        assert get_order_requests.status_code == 200 and get_order_requests.json()["success"] == True

        StellarBurgersApi.delete_user(access)

    @allure.title('Проверка получения списка заказов пользователя без авторизации')
    @allure.description('Отсылаем запрос на получение списка заказов конкретного пользователя не авторизуясь перед этим. Проверяем, что вернулась ошибка')
    def test_get_order_list_certain_user_without_authorization(self):
        get_order_requests = StellarBurgersApi.get_order_certain_user("")

        assert get_order_requests.status_code == 401 and get_order_requests.json()["success"] == False
