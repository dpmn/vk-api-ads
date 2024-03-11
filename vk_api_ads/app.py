import json
import webbrowser
from uuid import uuid4
from urllib.parse import urlencode, urlparse, parse_qs
from requests import request as http_request
from vk_api_ads.exceptions import VKAppClientError, VKAppApiError


class VKApp:
    def __init__(self, app_id: int, service_token: str):
        """
        Клиент для взаимодействия с приложением VK.
        :param app_id: Идентификатор приложения.
        :param service_token: Сервисный токен приложения.
        """
        self._app_id = app_id
        self.__service_token = service_token

    def get_silent_token(self, redirect_uri: str):
        """
        Генерирует токен (Silent token) для предварительного получения данных пользователя.
        :param redirect_uri: Адрес, на который будет передан токен.
        :return:
        """
        params = {
            'uuid': uuid4(),
            'app_id': self._app_id,
            'response_type': 'silent_token',
            'redirect_uri': redirect_uri
        }
        url = f'https://id.vk.com/auth?{urlencode(params)}'
        webbrowser.open(url=url, new=2)

    def get_access_token(self, redirected_url: str, api_version: str = '5.131'):
        """
        Генерирует токен (Access token) для вызова методов API.
        :param redirected_url: Ссылка, которая содержит (Silent token)
        :param api_version:  Используемая версия API. По умолчанию 5.131.
        :return:
        """
        try:
            # Разбор URL для извлечения параметров
            parsed_url = urlparse(redirected_url)
            query_params = parse_qs(parsed_url.query)
            # Декодирование значения параметра 'payload' из строки запроса
            payload_json = query_params['payload'][0]
            # Преобразование строки JSON в словарь
            payload_dict = json.loads(payload_json)

            url = 'https://api.vk.com/method/auth.exchangeSilentAuthToken'
            params = {
                'v': api_version,
                'token': payload_dict['token'],
                'access_token': self.__service_token,
                'uuid': payload_dict['uuid']
            }
            # Запрос для получения access_token
            response = http_request('GET', url, params=params)
            response_json = response.json()

            if response.status_code == 200:
                if error_msg := response_json.get('error', None):
                    raise VKAppApiError(response.status_code, error_msg)
                else:
                    return response_json['response']
            else:
                raise VKAppApiError(response.status_code, response_json)
        except KeyError:
            raise VKAppClientError(KeyError)
