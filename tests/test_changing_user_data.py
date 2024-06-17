from stellarburgers_api import StellarBurgersApi
import data
import allure
from conftest import user

class TestChangingUserData:

    @allure.title('Проверяем изменение емейла с авторизацией')
    @allure.description('Создаём пользователя, авторизуемся им и меняем емейл. После проверки удаляем юзера')
    def test_change_email_with_authorization(self, user):
        auth_body = {
            "email": data.CREATE_USER_BODY["email"],
            "password": data.CREATE_USER_BODY["password"]
        }
        auth_user_requests = StellarBurgersApi.auth_user(auth_body)
        access = auth_user_requests.json()["accessToken"]
        change_email_requests = StellarBurgersApi.changing_user(access, data.CHANGE_EMAIL)

        assert change_email_requests.status_code == 200 and change_email_requests.json()["success"] == True


    @allure.title('Проверяем изменение имени с авторизацией')
    @allure.description('Создаём пользователя, авторизуемся им и меняем имя. После проверки удаляем юзера')
    def test_change_name_with_authorization(self, user):
        auth_body = {
            "email": data.CREATE_USER_BODY["email"],
            "password": data.CREATE_USER_BODY["password"]
        }
        auth_user_requests = StellarBurgersApi.auth_user(auth_body)
        access = auth_user_requests.json()["accessToken"]
        change_email_requests = StellarBurgersApi.changing_user(access, data.CHANGE_NAME)

        assert change_email_requests.status_code == 200 and change_email_requests.json()["success"] == True


    @allure.title('Проверяем изменение емейла без авторизации')
    @allure.description(
        'Создаём пользователя и меняем емейл, отправляя пустой accessToken. Проверяем, что вернулась ошибка. Текст ошибки: "You should be authorised". После проверки удаляем юзера')
    def test_change_email_without_authorization(self):
        change_email_requests = StellarBurgersApi.changing_user("", data.CHANGE_EMAIL)

        assert change_email_requests.status_code == 401 and change_email_requests.json()["message"] == data.CHANGE_DATA_WITHOUT_AUTHORIZATION

    @allure.title('Проверяем изменение имени без авторизации')
    @allure.description(
        'Создаём пользователя и меняем имя, отправляя пустой accessToken. Проверяем, что вернулась ошибка. Текст ошибки: "You should be authorised". После проверки удаляем юзера')
    def test_change_name_without_authorization(self):
        change_email_requests = StellarBurgersApi.changing_user("", data.CHANGE_NAME)

        assert change_email_requests.status_code == 401 and change_email_requests.json()["message"] == data.CHANGE_DATA_WITHOUT_AUTHORIZATION
