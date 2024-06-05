from stellarburgers_api import StellarBurgersApi
import data
import allure
import helper

class TestCreateOrder:

    @allure.title('Проверка создания заказа с авторизацией')
    @allure.description('Создаём пользователя, авторизуемся им и создаём заказ. Проверяем, что заказ создался. После проверки удаляем пользователя')
    def test_create_order_with_authorization(self):
        StellarBurgersApi.create_user(data.CREATE_USER_BODY)
        auth_body = {
            "email": data.CREATE_USER_BODY["email"],
            "password": data.CREATE_USER_BODY["password"]
        }
        auth_user_requests = StellarBurgersApi.auth_user(auth_body)
        access = auth_user_requests.json()["accessToken"]
        body_order = { "ingredients": helper.get_list_random_ingredients(6)}
        create_order_requests = StellarBurgersApi.create_order(access, body_order)

        assert create_order_requests.status_code == 200 and create_order_requests.json()["success"] == True

        StellarBurgersApi.delete_user(access)

    @allure.title('Проверка создания заказа неавторизованным пользователем')
    @allure.description('Создаём заказ без авторизации пользователя и проверяем, что он создался (Создать заказ != оформить заказ).')
    def test_create_order_without_authorization(self):
        body_order = {"ingredients": helper.get_list_random_ingredients(6)}
        create_order_requests = StellarBurgersApi.create_order("", body_order)

        assert create_order_requests.status_code == 200 and create_order_requests.json()["success"] == True


    @allure.title('Проверка создания заказа без ингредиентов')
    @allure.description('Создаём пользователя, авторизуемся им, затем создаём заказ без ингредиентов. Проверяем, что вернулась ошибка. Текст ошибки: "Ingredient ids must be provided". После проверки удаляем пользователя')
    def test_create_order_without_ingredients(self):
        StellarBurgersApi.create_user(data.CREATE_USER_BODY)
        auth_body = {
            "email": data.CREATE_USER_BODY["email"],
            "password": data.CREATE_USER_BODY["password"]
        }
        auth_user_requests = StellarBurgersApi.auth_user(auth_body)
        access = auth_user_requests.json()["accessToken"]
        body_order = {"ingredients": []}
        create_order_requests = StellarBurgersApi.create_order(access, body_order)

        assert create_order_requests.status_code == 400 and create_order_requests.json()["message"] == data.CREATE_ORDER_WITHOUT_INGREDIENTS_400_RESPONSE

        StellarBurgersApi.delete_user(access)

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов')
    @allure.description('Создаём пользователя, авторизуемся им и создаём заказ с рандомно сгенерированным хэшем ингредиентов. Проверяем, что вернулась 500 ошибка. После проверки удаляем пользователя')
    def test_create_order_with_invalid_hash_ingredients(self):
        StellarBurgersApi.create_user(data.CREATE_USER_BODY)
        auth_body = {
            "email": data.CREATE_USER_BODY["email"],
            "password": data.CREATE_USER_BODY["password"]
        }
        auth_user_requests = StellarBurgersApi.auth_user(auth_body)
        access = auth_user_requests.json()["accessToken"]
        body_order = data.RANDOM_HASH_INGREDIENTS
        create_order_requests = StellarBurgersApi.create_order(access, body_order)

        assert create_order_requests.status_code == 500

        StellarBurgersApi.delete_user(access)