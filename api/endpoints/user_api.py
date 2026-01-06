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

    def assert_if_user_authorized(self, err_msg = 'Юзер авторизован'):
        assert (self.access_token is None and
                self.refresh_token is None), err_msg

    def assert_if_user_not_authorized(self, err_msg = 'Юзер не авторизован'):
        assert (self.access_token is not None or
                self.refresh_token is not None), err_msg

    @allure.step('Проверка существования юзера')
    def is_user_exists(self, name, email, password):
        """
        Функция проверяет существует ли данный пользователь.

        Уникальным должен быть email, name и password могут совпадать.
        Проверка осуществляется попыткой регистрации, если данный юзер не
        существует, то регистрация проходит успешно и юзер сразу же удаляется.

        При проверке требуется отсутствие авторизации, иначе выдаст
        исключение.

        :param name: имя юзера (не уникальное)
        :param email: email юзера (уникальный)
        :param password: пароль юзера (не уникальный)
        :return: boolean
        """

        self.assert_if_user_authorized(
            'При проверке существования юзера, '
            'требуется отсутствие авторизации')

        response = requests.post(
            url = APIUrls.registration,
            json = {
                'email': email,
                'password': password,
                'name': name
            },
            headers = Headers.common
        )

        is_exists = (not response.json()['success']
            and response.json()['message'] == 'User already exists')

        if not is_exists:
            self.authorization(email, password)
            self.user_delete()

        return is_exists

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

    @allure.step('Logout юзера')
    def logout(self):
        self.assert_if_user_not_authorized('Для выхода из системы юзер '
                                           'должен быть авторизован')

        self.response = requests.post(
            url = APIUrls.logout,
            json = {
                'token': self.refresh_token
            },
            headers = Headers.common
        )

        self.access_token = None
        self.refresh_token = None

    @allure.step('Запрос accessToken авторизованного пользователя')
    def get_access_token(self):
        return self.access_token

    @allure.step('Запрос refreshToken авторизованного пользователя')
    def get_refresh_token(self):
        return self.refresh_token

    @allure.step('Запрос данных юзера')
    def userdata(self):
        self.assert_if_user_not_authorized('Для запроса данных юзер '
                                           'должен быть авторизован')

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
        self.assert_if_user_not_authorized('Для удаления юзера юзер '
                                           'должен быть авторизован')

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