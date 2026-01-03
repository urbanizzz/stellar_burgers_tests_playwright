
class MainPageLocators:
    account_btn = '//a[@href="/account"]'
    drop_area = '//div[contains(@class, "constructor-element_pos_top")]'
    basket_list_element = '//span[@class="constructor-element__text"]'

    @staticmethod
    def ingredient_locator(name):
        return f'//p[text()="{name}"]'
