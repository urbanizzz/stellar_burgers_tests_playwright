import pytest

from playwright.sync_api import Page

from api.endpoints.user_api import UserAPI
from ui.data.test_data import RegistrationData

@pytest.fixture
def not_authorized_user(page: Page):
    return {
        'page': page
    }

@pytest.fixture
def for_registration(not_authorized_user):
    page = not_authorized_user['page']
    reg_data = RegistrationData()

    yield {
        'page': page,
        'reg_data': reg_data
    }

    # TODO: переделать фикстуры

@pytest.fixture
def authorized_user(page: Page):
    reg_data = RegistrationData()
    user = UserAPI()
    user.registration(reg_data.name, reg_data.email, reg_data.password)
    user.authorization(reg_data.email, reg_data.password)
    yield {
        'page': page,
        'accessToken': user.get_access_token(),
        'refreshToken': user.get_refresh_token()
    }
    user.user_delete()


