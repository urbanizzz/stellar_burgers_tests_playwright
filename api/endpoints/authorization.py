import requests
import allure

from api.data.api_urls import APIUrls
from api.data.headers import Headers
from api.endpoints.endpoints import Endpoints


class Authorization(Endpoints):
    # access_token = None
    # refresh_token = None

    @allure.step('Авторизация в системе')
    def __init__(self, email, password):
        self.response = requests.post(
            url = APIUrls.authorization,
            json = {
                'email': email,
                'password': password
            },
            headers = Headers.common
        )

        self.check_response_status_code_200(self.response.text)
        self.response_json = self.response.json()
        # self.access_token = self.response_json['accessToken']
        # self.refresh_token = self.response_json['refreshToken']

    @allure.step('Запрос accessToken авторизованного пользователя')
    def get_access_token(self):
        return self.response_json['accessToken']

    @allure.step('Запрос refreshToken авторизованного пользователя')
    def get_refresh_token(self):
        return self.response_json['refreshToken']

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
        print(self.response_json)
