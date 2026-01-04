
class MainPageLocators:
    account_btn = '//a[@href="/account"]'
    drop_area = '//div[contains(@class, "constructor-element_pos_top")]'
    basket_list_element = '//span[@class="constructor-element__text"]'

    @staticmethod
    def ingredient_locator(name):
        return f'//p[text()="{name}"]'

class LoginLocators:
    email_field = '//input[@name="name"]'
    password_field = '//input[@name="Пароль"]'
    submit_btn = '//button[text()="Войти"]'
    register_btn = '//a[@href="/register"]'
