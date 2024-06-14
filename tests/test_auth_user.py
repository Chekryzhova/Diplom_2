from stellarburgers_api import StellarBurgersApi
import data
import allure
from conftest import user

class TestAuthUser:

    @allure.title('Проверка авторизации юзера')
    @allure.description('Регистрируемся юзером, затем авторизуемся им. После проверки удаляем юзера')
    def test_auth_with_existing_user(self, user):
        auth_body = {
            "email": data.CREATE_USER_BODY["email"],
            "password": data.CREATE_USER_BODY["password"]
        }
        auth_user_requests = StellarBurgersApi.auth_user(auth_body)

        assert auth_user_requests.status_code == 200 and auth_user_requests.json()["success"] == True


    @allure.title('Проверка авторизации с неверным логином и паролем')
    @allure.description('Регистрируем пользователя, затем авторизуемся с неверным логином и паролем. Проверяем, что юзер не авторизовался и текст ошибки: "email or password are incorrect". После проверки удаляем юзера')

    def test_auth_with_incorrect_auth_body(self, user):
        auth_user_requests = StellarBurgersApi.auth_user(data.INCORRECT_AUTH_BODY)

        assert auth_user_requests.status_code == 401 and auth_user_requests.json()["message"] == data.AUTH_USER_WITH_INCORRECT_AUTH_BODY_401_RESPONSE
