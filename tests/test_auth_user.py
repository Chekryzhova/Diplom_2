from stellarburgers_api import StellarBurgersApi
import data
import allure

class TestAuthUser:

    @allure.title('Проверка авторизации юзера')
    @allure.description('Регистрируемся юзером, затем авторизуемся им. После проверки удаляем юзера')
    def test_auth_with_existing_user(self):
        StellarBurgersApi.create_user(data.CREATE_USER_BODY)
        auth_body = {
            "email": data.CREATE_USER_BODY["email"],
            "password": data.CREATE_USER_BODY["password"]
        }
        auth_user_requests = StellarBurgersApi.auth_user(auth_body)
        access = auth_user_requests.json()["accessToken"]

        assert auth_user_requests.status_code == 200 and auth_user_requests.json()["success"] == True

        StellarBurgersApi.delete_user(access)

    @allure.title('Проверка авторизации с неверным логином и паролем')
    @allure.description('Регистрируем пользователя, затем авторизуемся с неверным логином и паролем. Проверяем, что юзер не авторизовался и текст ошибки: "email or password are incorrect". После проверки удаляем юзера')

    def test_auth_with_incorrect_auth_body(self):
        create_user_requests = StellarBurgersApi.create_user(data.CREATE_USER_BODY)
        access = create_user_requests.json()["accessToken"]
        auth_body = {
            "email": "Sail",
            "password": "12345"
        }
        auth_user_requests = StellarBurgersApi.auth_user(auth_body)

        assert auth_user_requests.status_code == 401 and auth_user_requests.json()["message"] == data.AUTH_USER_WITH_INCORRECT_AUTH_BODY_401_RESPONSE

        StellarBurgersApi.delete_user(access)