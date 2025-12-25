import allure

class Endpoints:
    response = None
    response_json = None

    @allure.step('Проверка status_code == 200')
    def check_response_status_code_200(self, message):
        assert self.response.status_code == 200, message

    @allure.step('Проверка status_code == 404')
    def check_response_status_code_404(self, message):
        assert self.response.status_code == 404, message
