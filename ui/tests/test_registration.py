import time

import pytest
import allure

from ui.data.test_data import RegistrationData
from ui.pages.login_page import LoginPage
from ui.data.test_data import AuthData
from ui.pages.registration_page import RegistrationPage
from ui.pages.login_page import LoginPage


@allure.title('Проверка регистрации нового пользователя')
@allure.description('Успешная регистрация')
@pytest.mark.registration
def test_registration(not_authorized_user):
    reg_data = RegistrationData()
    reg_data.print_data()

    page = RegistrationPage(not_authorized_user['page'])
    page.open_registration_page()
    page.fill_name_field(reg_data.name)
    page.fill_email_field(reg_data.email)
    page.fill_password_field(reg_data.password)
    page.submit_btn_click()

    page = LoginPage(not_authorized_user['page'])
    page.open_main_page()
    page.click_account_button_on_main_page()
    page.fill_email_field(reg_data.email)
    page.fill_password_field(reg_data.password)
    page.submit_btn_click()
    page.check_login(reg_data.name, reg_data.email)

    time.sleep(3)
