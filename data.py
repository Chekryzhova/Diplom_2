import random

CREATE_USER_BODY = {
    "email": "Katy1777@maill.com",
    "password": "qwerty",
    "name": "Katy"
}

RANDOM_HASH_INGREDIENTS = {"ingredients": [f'Aghulnvfdq{random.randint(10000000000000, 99999999999999)}']}

CREATE_SIMILAR_USER_403_RESPONSE = "User already exists"
CREATE_USER_WITHOUT_PASSWORD_403_RESPONSE = "Email, password and name are required fields"
AUTH_USER_WITH_INCORRECT_AUTH_BODY_401_RESPONSE = "email or password are incorrect"
CHANGE_DATA_WITHOUT_AUTHORIZATION = "You should be authorised"
CREATE_ORDER_WITHOUT_INGREDIENTS_400_RESPONSE = "Ingredient ids must be provided"
INCORRECT_AUTH_BODY = {
            "email": "Sail",
            "password": "12345"
        }

CHANGE_EMAIL = {
            "email": "Cat7@gmail.com"
        }

CHANGE_NAME = {
            "name": "Cat"
        }