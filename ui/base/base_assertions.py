import allure

from playwright.sync_api import Page, expect

from ui.base.base_page import BasePage


class Assertions(BasePage):
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    @allure.step('Проверка на равенство фактического и ожидаемого значений')
    def assert_equal(self, actual, expected, err_msg: str = None) -> None:
        """
        :param actual: Фактическое значение
        :param expected: Ожидаемое значение
        :param err_msg: Сообщение об ошибке
        """
        assert actual == expected, (
            f'{err_msg if err_msg else "Значения должны быть равны"}\n:'
            f'Actual: {actual}\nExpected: {expected}'
        )
