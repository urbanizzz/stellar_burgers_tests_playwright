import time
import requests
import pytest

from playwright.sync_api import sync_playwright, Page
from api.endpoints.user_api import UserAPI
from ui.data.test_data import RegistrationData


# with sync_playwright() as p:
#     # browser = p.chromium.launch(headless=False)
#     browser = p.webkit.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.google.com/")
#     print(page.title())
#     time.sleep(5)

def ttest_open_browser(page: Page):
    page.goto("https://google.com")
    print(page.title())

def ttest_navigation(page: Page):
    page.goto("https://google.com")
    page.goto("https://github.com")
    page.goto("https://yandex.ru")
    print(page.url)

    page.go_back()
    print(page.url)
    page.go_back()
    print(page.url)
    page.go_forward()
    print(page.url)

def ttest_locators(page: Page):
    page.goto("https://google.com")
    # el = page.get_by_role('combobox')
    # el = page.locator('#APjFqb')
    el = page.locator('//div').filter(has=page.locator('#APjFqb'))

    el.fill('github.com')
    time.sleep(3)

email = 'murban@mail.com'
password = 'qweasdzxc'
name = 'urban'
name1 = 'qwe123asd456zxc789'
email1 = f'{name1}@mail.com'

base_url = 'https://stellarburgers.education-services.ru'
base_api_url = f'{base_url}/api'
authorization_url = f'{base_api_url}/auth/login'
userdata_url = f'{base_api_url}/auth/user'
headers = {
    'Content-Type': 'application/json'
}
lk_locator ='//a[@href="/account"]'

# @pytest.mark.test
def ttest_api():
    # authorization
    response = requests.post(
        url = authorization_url,
        json = {
            'email': email,
            'password': password
        },
        headers = headers
    )

    assert response.status_code == 200, response.text

    # get userdata
    response_json = response.json()
    access_token = response_json['accessToken']
    refresh_token = response_json['refreshToken']
    print(f'\naccess_token: {access_token}')
    print(f'refresh_token: {refresh_token}')

    get_response = requests.get(
        url = userdata_url,
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'{access_token}'
        }
    )

    assert get_response.status_code == 200, get_response.text

    print(get_response.json())

# @pytest.mark.testapi
def ttest_api_class():
    print()
    user = UserAPI()
    lname = 'murban'
    lemail = 'murban@mail.com'
    lpassword = 'qweasdzxc'
    # if user.is_user_exists(lname, lemail, lpassword):
    #     print(f'User exists')
    # else:
    #     print(f'User does not exists')

    # reg_data = RegistrationData()
    # reg_data.print_data()
    # user.registration(reg_data.name, reg_data.email, reg_data.password)
    # user.authorization(reg_data.email, reg_data.password)
    user.authorization(lemail, lpassword)
    print(user.get_access_token())
    print(user.get_refresh_token())
    print(user.userdata())
    user.logout()
    print(user.get_access_token())
    print(user.get_refresh_token())
    print(user.userdata())

    # user.authorization(lemail2, lpassword)
    # print(user.get_access_token())
    # print(user.get_refresh_token())
    # print(user.userdata())
    # print(user.user_delete())

# @pytest.mark.userdel
def ttest_user_delete():
    print()
    user = UserAPI()
    lname = 'murban1'
    lemail = 'murban1@mail.com'
    lpassword = 'qweasdzxc'
    user.authorization(lemail, lpassword)
    print(user.get_access_token())
    print(user.get_refresh_token())
    print(user.userdata())
    print(user.user_delete())


def ttest_fixture(authorized_user):
    el = authorized_user.locator(lk_locator)
    el.click()

# @pytest.mark.test
def ttest_role(not_authorized_user):
    page = not_authorized_user['page']
    page.goto(base_url)
    print(page.url)
    page.get_by_role('button', name='Войти в аккаунт').click()
    print(page.url)
    page.get_by_role('label', name='Email').get_by_role('input').fill(
        email, timeout=3000)

# @pytest.mark.test
def ttest_get_url(page: Page):
    page.goto("https://google.com")
    print(page.url)

# @pytest.mark.test
def ttest_name_gen():
    print()
    for _ in range(3):
        user = RegistrationData()
        print(f'{user.name}, {user.email}, {user.password}')
