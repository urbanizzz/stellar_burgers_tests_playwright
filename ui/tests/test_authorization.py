import pytest
import allure

from ui.pages.login_page import LoginPage
from ui.data.test_data import AuthData


@allure.title('Проверка авторизации')
@allure.description('Успешная авторизация')
@pytest.mark.authorization
def test_login(not_authorized_user):
    page = LoginPage(not_authorized_user['page'])
    page.open_main_page()
    page.click_account_button_on_main_page()
    page.fill_email_field(AuthData.email)
    page.fill_password_field(AuthData.password)
    page.submit_btn_click()
    page.check_login(AuthData.name, AuthData.email)
