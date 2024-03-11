# vk-api-ads
Экспортируйте статистику по рекламным объектам из старого кабинета рекламы VK

## Получение токена для работы с API
Для начала работы с API необходимо создать приложение по этой ссылке https://id.vk.com/about/business/go.

Инструкция для создания приложения: https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/create-application.

После создания приложения, потребуется сохранить ID приложения и Сервисный ключ доступа -- они понадобятся для получения токена.

Создайте экземпляр класса VKApp и вызовите метод get_silent_token(). Откроется браузер, подтвердите вход. После редиректа скопируйте ссылку и
отправьте её в методе get_access_token().

## Другой вариант получения токена (старый способ)
https://dev.vk.com/ru/api/access-token/authcode-flow-user

Перейти по ссылке https://oauth.vk.com/authorize?client_id=<CLIENT_ID>&display=page&redirect_uri=<REDIRECT_URI>&scope=ads&response_type=code&v=5.131&state=give_my_token
Затем по ссылке: https://oauth.vk.com/access_token?client_id=<CLIENT_ID>&client_secret=<CLIENT_SECRET>&redirect_uri=<REDIRECT_URI>&code=<CODE>
