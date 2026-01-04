import pytest

from playwright.sync_api import Page

from api.endpoints.authorization import Authorization
from ui.data.test_data import AuthData


@pytest.fixture
def authorized_user(page: Page):
    obj = Authorization(AuthData.email, AuthData.password)
    obj.check_response_status_code_200('Не прошла авторизация по API')
    return {
        'page': page,
        'accessToken': obj.get_access_token(),
        'refreshToken': obj.get_refresh_token()
    }

@pytest.fixture
def not_authorized_user(page: Page):
    return {
        'page': page
    }
