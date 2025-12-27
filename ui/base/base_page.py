import allure

from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    @allure.suite('Открытие страницы')
    def open(self, url: str):
        self.page.goto(url)

    @allure.step('Клик на элементе')
    def click_on_element(self, locator):
        self.page.click(selector=locator)

    @allure.step('Заполнение поля текстом')
    def fill_field(self, locator, text):
        self.page.fill(selector=locator, value=text)

    @allure.step('Определение переменной в локальном хранилище')
    def set_item(self, item, value):
        self.page.evaluate(f'localStorage.setItem("{item}", "{value}");')

    @allure.step('Закрытие страницы')
    def close(self):
        self.page.close()
