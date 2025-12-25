import pytest
import allure

from playwright.sync_api import Page

from api.endpoints.authorization import Authorization
from ui.data.test_data import AuthData
from ui.data.urls import Urls


@allure.step('Подготовка фикстуры с залогиненым юзером')
@pytest.fixture
def authorized_user(page: Page):
    obj = Authorization(AuthData.email, AuthData.password)
    obj.check_response_status_code_200('Не прошла авторизация по API')
    page.goto(Urls.base)
    page.evaluate(f'localStorage.setItem("accessToken", '
                  f'"{obj.get_access_token()}");')
    page.evaluate(f'localStorage.setItem("refreshToken", '
                  f'"{obj.get_refresh_token()}");')
    return page
