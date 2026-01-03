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

    @allure.step('Перетаскивание элемента')
    def drag_and_drop(self, drag_locator, drop_locator):
        self.page.locator(drag_locator).drag_to(
            self.page.locator(drop_locator))

    @allure.step('Чтение текста из списка элементов')
    def get_text_content_from_list(self, locator):
        return [el.text_content() for el in self.page.locator(locator).all()]
