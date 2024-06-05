from stellarburgers_api import StellarBurgersApi
import data
import allure

class TestChangingUserData:

    @allure.title('Проверяем изменение емейла с авторизацией')
    @allure.description('Создаём пользователя, авторизуемся им и меняем емейл. После проверки удаляем юзера')
    def test_change_email_with_authorization(self):
        StellarBurgersApi.create_user(data.CREATE_USER_BODY)
        auth_body = {
            "email": data.CREATE_USER_BODY["email"],
            "password": data.CREATE_USER_BODY["password"]
        }
        auth_user_requests = StellarBurgersApi.auth_user(auth_body)
        access = auth_user_requests.json()["accessToken"]
        change_body = {
            "email": "Cat7@gmail.com"
        }
        change_email_requests = StellarBurgersApi.changing_user(access, change_body)

        assert change_email_requests.status_code == 200 and change_email_requests.json()["success"] == True

        StellarBurgersApi.delete_user(access)

    @allure.title('Проверяем изменение имени с авторизацией')
    @allure.description('Создаём пользователя, авторизуемся им и меняем имя. После проверки удаляем юзера')
    def test_change_name_with_authorization(self):
        StellarBurgersApi.create_user(data.CREATE_USER_BODY)
        auth_body = {
            "email": data.CREATE_USER_BODY["email"],
            "password": data.CREATE_USER_BODY["password"]
        }
        auth_user_requests = StellarBurgersApi.auth_user(auth_body)
        access = auth_user_requests.json()["accessToken"]
        change_body = {
            "name": "Cat"
        }
        change_email_requests = StellarBurgersApi.changing_user(access, change_body)

        assert change_email_requests.status_code == 200 and change_email_requests.json()["success"] == True

        StellarBurgersApi.delete_user(access)

    @allure.title('Проверяем изменение емейла без авторизации')
    @allure.description(
        'Создаём пользователя и меняем емейл, отправляя пустой accessToken. Проверяем, что вернулась ошибка. Текст ошибки: "You should be authorised". После проверки удаляем юзера')
    def test_change_email_without_authorization(self):
        create_user_requests = StellarBurgersApi.create_user(data.CREATE_USER_BODY)
        access = create_user_requests.json()["accessToken"]
        change_body = {
            "email": "Cat7@gmail.com"
        }
        change_email_requests = StellarBurgersApi.changing_user("", change_body)

        assert change_email_requests.status_code == 401 and change_email_requests.json()["message"] == data.CHANGE_DATA_WITHOUT_AUTHORIZATION

        StellarBurgersApi.delete_user(access)

    @allure.title('Проверяем изменение имени без авторизации')
    @allure.description(
        'Создаём пользователя и меняем имя, отправляя пустой accessToken. Проверяем, что вернулась ошибка. Текст ошибки: "You should be authorised". После проверки удаляем юзера')
    def test_change_name_without_authorization(self):
        create_user_requests = StellarBurgersApi.create_user(data.CREATE_USER_BODY)
        access = create_user_requests.json()["accessToken"]
        change_body = {
            "name": "Cat77"
        }
        change_email_requests = StellarBurgersApi.changing_user("", change_body)

        assert change_email_requests.status_code == 401 and change_email_requests.json()["message"] == data.CHANGE_DATA_WITHOUT_AUTHORIZATION

        StellarBurgersApi.delete_user(access)