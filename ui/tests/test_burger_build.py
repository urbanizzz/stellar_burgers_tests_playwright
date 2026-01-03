import time

import allure
import pytest

from ui.data.test_data import TestData
from ui.pages.main_page import MainPage


@allure.title('Создание бургера')
@allure.description('Успешное создание бургера')
@pytest.mark.burger_build
def test_burger_build(authorized_user):
    page = MainPage(authorized_user['page'])
    page.open_main_page()
    page.set_item('accessToken', authorized_user['accessToken'])
    page.set_item('refreshToken', authorized_user['refreshToken'])

    page.build_burger(TestData.burger)
    actual_burger = page.get_basket_list()
    print(*actual_burger, sep='\n')

    assert TestData.burger == actual_burger, (f'Ожидаемый бургер: '
        f'{TestData.burger}, а фактически: {actual_burger}')
