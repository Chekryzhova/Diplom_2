from stellarburgers_api import StellarBurgersApi
import pytest
import data

@pytest.fixture(scope='function')
def user():
    create_user_requests = StellarBurgersApi.create_user(data.CREATE_USER_BODY)
    access = create_user_requests.json().get("accessToken")

    yield create_user_requests

    StellarBurgersApi.delete_user(access)