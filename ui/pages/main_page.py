import allure

from playwright.sync_api import Page

from ui.base.base_assertions import Assertions
from ui.base.base_page import BasePage
from ui.data.urls import Urls
from ui.data.locators import MainPageLocators as MPL

class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, Urls.base)
        self.assertions = Assertions(page, Urls.base)

    @allure.step('Открытие главной страницы')
    def open_main_page(self):
        self.open(self.base_url)

    @allure.step('Создание бургера из данных ингредиентов')
    def build_burger(self, burger):
        for ingredient in burger:
            self.drag_and_drop(
                MPL.ingredient_locator(ingredient), MPL.drop_area)

    @allure.step('Получение списка ингредиентов бургера')
    def get_basket_list(self):
        ls = self.get_text_content_from_list(MPL.basket_list_element)

        ls[0] = ls[0][:-7]  # отрезать слово "(верх)" от названия булки
        return ls[:-1]      # отрезать второе название булки
