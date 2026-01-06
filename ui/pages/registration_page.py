import allure

from playwright.sync_api import Page

from ui.base.base_assertions import Assertions
from ui.base.base_page import BasePage
from ui.data.urls import Urls
from ui.data.locators import RegistrationLocators as RL
from ui.data.locators import MainPageLocators as MPL
from ui.data.locators import LoginLocators as LL
from ui.data.locators import AccountLocators as AL

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, Urls.base)
        self.assertions = Assertions(page, Urls.base)

    @allure.step('Открытие страницы регистрации')
    def open_registration_page(self):
        self.open(self.base_url)
        self.click_on_element(MPL.account_btn)
        self.click_on_element(LL.registration_btn)

    @allure.step('Заполнение имени при регистрации')
    def fill_name_field(self, name):
        self.fill_field(RL.name_field, name)

    @allure.step('Заполнение email при регистрации')
    def fill_email_field(self, email):
        self.fill_field(RL.email_field, email)

    @allure.step('Заполнение пароля при регистрации')
    def fill_password_field(self, password):
        self.fill_field(RL.password_field, password)

    @allure.step('Клик по кнопке Зарегистрироваться')
    def submit_btn_click(self):
        self.click_on_element(RL.submit_btn)
