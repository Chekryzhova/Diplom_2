import allure
from stellarburgers_api import StellarBurgersApi
import data
import helper
from conftest import user


class TestCreateUser:

    @allure.title('Тест на успешное создание уникального пользователя')
    @allure.description('Генерируем рандомные данные для создания уникального пользователя и проверяем, что пользователь успешно создался. После проверки удаляем юзера')
    def test_success_create_user(self, user):

        assert user.status_code == 200 and user.json().get("success") == True



    @allure.title('Тест на создание двух одинаковых пользователей')
    @allure.description('Создаём одного юзера,затем создаём второго юзера с таким же набором данных. Проверяем, что второй юзер не создался и текст ошибки: "User already exists". После проверки удаляем юзера')
    def test_create_two_similar_user(self, user):
        create_similar_user = StellarBurgersApi.create_user(data.CREATE_USER_BODY)

        assert create_similar_user.status_code == 403 and create_similar_user.json()["message"] == data.CREATE_SIMILAR_USER_403_RESPONSE

    @allure.title('Проверяем, что если одного из полей нет, запрос возвращает ошибку')
    @allure.description('Создаём юзера без пароля и проверяем,что вернулась ошибка.  Текст ошибки: "Email, password and name are required fields". После проверки удаляем юзера')
    def test_create_user_without_password(self):
        body = helper.change_data_create_user("password", "")
        create_user_requests = StellarBurgersApi.create_user(body)

        assert create_user_requests.status_code == 403 and create_user_requests.json()["message"] == data.CREATE_USER_WITHOUT_PASSWORD_403_RESPONSE
