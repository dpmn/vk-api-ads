import json
from time import sleep
from requests import request as http_request
from vk_api_ads.exceptions import VKAdsClientError, VKAdsApiError


class VKAds:
    def __init__(self, access_token: str, **kwargs):
        self.__access_token = access_token
        self._api_endpoint = f'https://{kwargs.get("server_address", "api.vk.com")}/method'
        self._api_version = kwargs.get('api_version', '5.131')
        self._request_latency = kwargs.get('request_latency', 10)  # Базовая задержка между запросами API

    def _make_request(self, api_method: str, headers: dict, params: dict):
        """
        Общая функция отправки запросов к API.
        :param api_method: Название метода VK API.
        :param headers: Заголовки запроса.
        :param params: Параметры запроса.
        :return:
        """
        # Параметры для регулирования скорости выполнения повторных запросов.
        retry_count = 0
        # Параметры для запроса к API
        api_url = '/'.join([self._api_endpoint, api_method])
        headers.update({'Authorization': f'Bearer {self.__access_token}'})
        params.update({'v': self._api_version})

        while True:
            try:
                response = http_request('GET', url=api_url, headers=headers, params=params)
                # Принудительная обработка ответа в кодировке UTF-8
                response.encoding = 'utf-8'

                if response.status_code == 200:
                    return response
                elif response.status_code in (201, 202):
                    # Увеличение задержки с каждой неудачной попыткой
                    retry_count += 1
                    latency_time = self._request_latency * 2 ** retry_count
                    sleep(latency_time)
                    if latency_time >= 600:
                        # Сбрасываем счётчик, если время ожидания больше 10 минут
                        retry_count = 0
                else:
                    raise VKAdsApiError(response.status_code, response.json())
            except ConnectionError:
                raise VKAdsClientError(ConnectionError)

    def get_statistics(self, account_id: int, ids_type: str, ids: list, period: str, **kwargs):
        """
        Возвращает статистику показателей эффективности по рекламным объявлениям, кампаниям, клиентам или всему
        кабинету.
        :param account_id: Идентификатор рекламного кабинета.
        :param ids_type: Тип запрашиваемых объектов, которые перечислены в параметре ids.
        :param ids: Список запрашиваемых ID объектов. Максимум 2000 объектов.
        :param period: Способ группировки данных по датам.
        :param kwargs: Остальные параметры метода (https://dev.vk.com/ru/method/ads.getStatistics).
        :return:
        """
        api_method = 'ads.getStatistics'

        headers = {}
        params = {
            'account_id': account_id,
            'ids_type': ids_type,
            'ids': ','.join(ids),
            'period': period,
            'date_from': kwargs.get('date_from', '0'),
            'date_to': kwargs.get('date_to', '0')
        }

        if stats_fields := kwargs.get('stats_fields', None):
            params.update({'stats_fields': stats_fields})

        response = self._make_request(api_method, headers, params)
        return response.json()

    def get_campaigns(self, account_id: int, **kwargs):
        """
        Возвращает список кампаний рекламного кабинета.
        :param account_id: Идентификатор рекламного кабинета.
        :param kwargs: Остальные параметры метода (https://dev.vk.com/ru/method/ads.getCampaigns).
        :return:
        """
        api_method = 'ads.getCampaigns'
        campaign_ids = kwargs.get('campaign_ids', None)

        headers = {}
        params = {
            'account_id': account_id,
            'include_deleted': kwargs.get('include_deleted', 1),
            # Если параметр равен строке null, то выводиться будут все кампании.
            'campaign_ids': 'null' if campaign_ids is None else json.dumps(campaign_ids)
        }

        if client_id := kwargs.get('client_id', None):
            params.update({'client_id': client_id})

        if fields := kwargs.get('fields', None):
            params.update({'fields': fields})

        response = self._make_request(api_method, headers, params)
        return response.json()

    def get_ads(self, account_id: int, **kwargs):
        """
        Возвращает список рекламных объявлений.
        :param account_id: Идентификатор рекламного кабинета.
        :param kwargs: Остальные параметры метода (https://dev.vk.com/ru/method/ads.getAds).
        :return:
        """
        api_method = 'ads.getAds'

        # Опциональные параметры метода, которые надо сериализовать для запроса
        campaign_ids = kwargs.get('campaign_ids', None)
        ad_ids = kwargs.get('ad_ids', None)
        # Опциональные параметры метода, которые надо отправлять только если они явно указаны в параметрах метода
        optional_api_params = ('client_id', 'limit', 'offset')

        headers = {}
        params = {
            'account_id': account_id,
            'include_deleted': kwargs.get('include_deleted', 1),
            'only_deleted': kwargs.get('only_deleted', 0),
            # Если параметр campaign_ids равен null, то будут выводиться рекламные объявления всех кампаний.
            'campaign_ids': 'null' if campaign_ids is None else json.dumps(campaign_ids),
            # Если параметр ad_ids равен null, то будут выводиться все рекламные объявления.
            'ad_ids': 'null' if ad_ids is None else json.dumps(ad_ids)
        }
        # Добавление опциональных параметров, если они присутствуют в запросе
        for param_name in optional_api_params:
            if param_value := kwargs.get(param_name, None):
                params.update({param_name: param_value})

        response = self._make_request(api_method, headers, params)
        return response.json()

    def get_ads_layout(self, account_id: int, **kwargs):
        """
        Возвращает описания внешнего вида рекламных объявлений.
        :param account_id: Идентификатор рекламного кабинета.
        :param kwargs: Остальные параметры метода (https://dev.vk.com/ru/method/ads.getAdsLayout).
        :return:
        """
        api_method = 'ads.getAdsLayout'

        # Опциональные параметры метода, которые надо сериализовать для запроса
        campaign_ids = kwargs.get('campaign_ids', None)
        ad_ids = kwargs.get('ad_ids', None)
        # Опциональные параметры метода, которые надо отправлять только если они явно указаны в параметрах метода
        optional_api_params = ('client_id', 'limit', 'offset')

        headers = {}
        params = {
            'account_id': account_id,
            'include_deleted': kwargs.get('include_deleted', 1),
            'only_deleted': kwargs.get('only_deleted', 0),
            # Если параметр campaign_ids равен null, то будут выводиться рекламные объявления всех кампаний.
            'campaign_ids': 'null' if campaign_ids is None else json.dumps(campaign_ids),
            # Если параметр ad_ids равен null, то будут выводиться все рекламные объявления.
            'ad_ids': 'null' if ad_ids is None else json.dumps(ad_ids)
        }
        # Добавление опциональных параметров, если они присутствуют в запросе
        for param_name in optional_api_params:
            if param_value := kwargs.get(param_name, None):
                params.update({param_name: param_value})

        response = self._make_request(api_method, headers, params)
        return response.json()
