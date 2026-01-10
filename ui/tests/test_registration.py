import pytest
import allure

from ui.pages.registration_page import RegistrationPage
from ui.pages.login_page import LoginPage


@allure.title('Проверка регистрации нового пользователя')
@allure.description('Успешная регистрация')
@pytest.mark.smoke
@pytest.mark.registration
def test_registration(for_registration):
    name = for_registration['name']
    email = for_registration['email']
    password = for_registration['password']

    page = RegistrationPage(for_registration['page'])
    page.open_registration_page()
    page.fill_name_field(name)
    page.fill_email_field(email)
    page.fill_password_field(password)
    page.submit_btn_click()

    page = LoginPage(for_registration['page'])
    page.open_main_page()
    page.click_account_button_on_main_page()
    page.fill_email_field(email)
    page.fill_password_field(password)
    page.submit_btn_click()
    page.check_login(name, email)
