import requests
import allure

from api.data.api_urls import APIUrls
from api.data.headers import Headers
from api.endpoints.endpoints import Endpoints


class UserAPI(Endpoints):

    def __init__(self):
        super().__init__()
        self.access_token = None
        self.refresh_token = None

    @allure.step('Авторизация существующего юзера')
    def authorization(self, email, password):
        self.response = requests.post(
            url = APIUrls.authorization,
            json = {
                'email': email,
                'password': password
            },
            headers = Headers.common
        )

        self.response_json = self.response.json()
        self.check_success('Ошибка авторизации: неправильный email или пароль')
        self.access_token = self.response_json['accessToken']
        self.refresh_token = self.response_json['refreshToken']

    @allure.step('Регистрация нового юзера')
    def registration(self, name, email, password):
        self.response = requests.post(
            url = APIUrls.registration,
            json = {
                'email': email,
                'password': password,
                'name': name
            },
            headers = Headers.common
        )

        self.response_json = self.response.json()
        self.check_success()

    @allure.step('Запрос accessToken авторизованного пользователя')
    def get_access_token(self):
        return self.access_token

    @allure.step('Запрос refreshToken авторизованного пользователя')
    def get_refresh_token(self):
        return self.refresh_token

    @allure.step('Запрос данных юзера')
    def userdata(self):
        headers_with_access_token = {
            **Headers.common,
            'Authorization': self.access_token
        }
        self.response = requests.get(
            url = APIUrls.userdata,
            headers = headers_with_access_token
        )

        self.response_json = self.response.json()
        self.check_success()

        return self.response_json['user']

    @allure.step('Удаление юзера')
    def user_delete(self):
        headers_with_access_token = {
            **Headers.common,
            'Authorization': self.access_token
        }
        self.response = requests.delete(
            url = APIUrls.user_delete,
            headers = headers_with_access_token
        )

        self.response_json = self.response.json()
        self.check_success()
        self.access_token = None
        self.refresh_token = None

        return 'User deleted'