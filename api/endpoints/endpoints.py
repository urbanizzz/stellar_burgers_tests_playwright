import allure

class Endpoints:

    def __init__(self):
        self.response = None
        self.response_json = None

    @allure.step('Проверка status_code == 200')
    def check_response_status_code_200(
        self,
        err_msg = f'Status code is not 200'
    ):
        assert self.response.status_code == 200, err_msg

    @allure.step('Проверка status_code == 404')
    def check_response_status_code_404(
        self,
        err_msg = f'Status code is not 404'
    ):
        assert self.response.status_code == 404, err_msg

    @allure.step('Проверка успешности запроса, путем response["success"] == '
                 'true')
    def check_success(
        self,
        err_msg = None
    ):
        if not self.response_json['success']:
            err_msg = self.response_json['message'] if err_msg is None else (
                err_msg)
        assert self.response_json['success'], err_msg
