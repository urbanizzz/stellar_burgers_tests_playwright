import pytest

from playwright.sync_api import Page

from api.endpoints.authorization import Authorization
from ui.base.base_page import BasePage
from ui.data.test_data import AuthData
from ui.data.urls import Urls


@pytest.fixture
def authorized_user(page: Page):
    obj = Authorization(AuthData.email, AuthData.password)
    obj.check_response_status_code_200('Не прошла авторизация по API')
    page = BasePage(page, Urls.base)
    page.open(Urls.base)
    page.set_item('accessToken', obj.get_access_token())
    page.set_item('refreshToken', obj.get_refresh_token())
    yield page
    page.close()
