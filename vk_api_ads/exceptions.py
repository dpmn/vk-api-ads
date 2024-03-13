class VKAppClientError(Exception):
    def __init__(self, original_exception, message='VKApp Client Error'):
        self.original_exception = original_exception
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.original_exception}'


class VKAppApiError(Exception):
    def __init__(self, status_code, message='VKApp API Error'):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} (Статус код: {self.status_code})'


class VKAdsClientError(Exception):
    def __init__(self, original_exception, message='VKAds Client Error'):
        self.original_exception = original_exception
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.original_exception}'


class VKAdsApiError(Exception):
    def __init__(self, error_code, error_msg, request_params):
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_params = request_params

    def __str__(self):
        return f'{self.error_msg} (Код ошибки: {self.error_code}) Параметры запроса: {self.request_params}'
