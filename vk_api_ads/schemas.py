from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date


class __BaseSchema(BaseModel):
    pass


# Модели для сложносоставных полей.
class EventRetargetingGroup(BaseModel):
    """
    Схема поля events_retargeting_groups в модели AdSchema.
    """
    id: Optional[int] = Field(default=None, description='Идентификатор группы ретаргетинга.')
    value: Optional[List[int]] = Field(default=None, description='Массив событий.')


class StatisticItemSchema(BaseModel):
    """
    Структура поля stats в модели StatisticSchema.
    """
    day: Optional[date] = Field(default=None, description='День в формате YYYY-MM-DD.')
    month: Optional[str] = Field(default=None, description='Месяц в формате YYYY-MM.')
    overall: Optional[int] = Field(default=None, description='1, если период равен overall.')
    spent: Optional[float] = Field(default=0.0, description='Потраченные средства.')
    impressions: Optional[int] = Field(default=0, description='Просмотры.')
    clicks: Optional[int] = Field(default=0, description='Клики.')
    reach: Optional[int] = Field(default=0, description='Охват.')
    join_rate: Optional[int] = Field(default=0, description='Вступления в группу или подписки.')
    uniq_views_count: Optional[int] = Field(default=0, description='Количество уникальных просмотров.')
    link_external_clicks: Optional[int] = Field(
        default=0,
        description='Количество уникальных переходов по внешним ссылкам.'
    )
    ctr: Optional[float] = Field(default=None, description='CTR.')
    effective_cost_per_click: Optional[float] = Field(default=None, description='eCPC.')
    effective_cost_per_mille: Optional[float] = Field(default=None, description='eCPM.')
    effective_cpf: Optional[float] = Field(default=None, description='eCPF.')


# Основные модели.
class CampaignSchema(__BaseSchema):
    """
    Модель кампании рекламного кабинета.
    https://dev.vk.com/ru/method/ads.getCampaigns
    """
    id: Optional[int] = Field(
        default=None,
        description='Идентификатор кампании.'
    )
    type: Optional[str] = Field(
        default=None,
        description='Тип кампании.'
    )
    name: Optional[str] = Field(
        default=None,
        description='Название кампании.'
    )
    status: Optional[int] = Field(
        default=None,
        description='Статус кампании: 0 — кампания остановлена; 1 — кампания запущена; 2 — кампания удалена.'
    )
    day_limit: Optional[float] = Field(
        default=None,
        description='Дневной лимит кампании в рублях. 0 — лимит не задан.'
    )
    all_limit: Optional[float] = Field(
        default=None,
        description='Общий лимит кампании в рублях. 0 — лимит не задан.'
    )
    start_time: Optional[int] = Field(
        default=None,
        description='Время запуска кампании в формате unixtime.'
    )
    stop_time: Optional[int] = Field(
        default=None,
        description='Время остановки кампании в формате unixtime.'
    )
    create_time: Optional[int] = Field(
        default=None,
        description='Время создания кампании в формате unixtime.'
    )
    update_time: Optional[int] = Field(
        default=None,
        description='Время обновления кампании в формате unixtime.'
    )
    goal_type: Optional[int] = Field(
        default=None,
        description=''
    )
    user_goal_type: Optional[int] = Field(
        default=None,
        description=''
    )
    views_limit: Optional[int] = Field(
        default=None,
        description=''
    )
    ads_count: Optional[int] = Field(
        default=None,
        description=''
    )
    is_cbo_enabled: Optional[bool] = Field(
        default=None,
        description=''
    )


class AdSchema(__BaseSchema):
    """
    Модель рекламного объявления.
    https://dev.vk.com/ru/method/ads.getAds
    """
    id: Optional[int] = Field(default=None, description='Идентификатор объявления.')
    campaign_id: Optional[int] = Field(default=None, description='Идентификатор кампании.')
    ad_format: Optional[int] = Field(default=None, description='Формат объявления.')
    cost_type: Optional[int] = Field(
        default=None,
        description='Тип оплаты. 0 — оплата за переходы; 1 — оплата за показы; 3 — оптимизированная оплата за показы.'
    )
    cpc: Optional[int] = Field(default=None, description='Цена за переход в копейках.')
    cpm: Optional[int] = Field(default=None, description='Цена за 1000 показов в копейках.')
    ocpm: Optional[int] = Field(default=None, description='Цена за действие для oCPM в копейках.')
    goal_type: Optional[int] = Field(
        default=None,
        description='Тип цели. Подробное описание: https://dev.vk.com/ru/method/ads/goals'
    )
    impressions_limit: Optional[int] = Field(
        default=None,
        description='Ограничение количества показов данного объявления на одного пользователя.'
    )
    impressions_limited: Optional[int] = Field(
        default=None,
        description='Признак того, что количество показов объявления на одного пользователя ограничено.'
    )
    ad_platform: Optional[str] = Field(default=None, description='Рекламные площадки.')
    ad_platform_no_wall: Optional[int] = Field(
        default=None,
        description='Ограничение "Не показывать на стенах сообществ".'
    )
    ad_platform_no_ad_network: Optional[int] = Field(
        default=None,
        description='Ограничение "Не показывать в рекламной сети".'
    )
    publisher_platforms: Optional[str] = Field(default=None, description='На каких площадках показывается объявление.')
    all_limit: Optional[float] = Field(default=None, description='Общий лимит объявления в рублях.')
    day_limit: Optional[float] = Field(default=None, description='Дневной лимит объявления в рублях.')
    autobidding: Optional[int] = Field(default=None, description='Автоматическое управление ценой.')
    autobidding_max_cost: Optional[int] = Field(
        default=None,
        description='Максимальное ограничение автоматической ставки в копейках.'
    )
    category1_id: Optional[int] = Field(default=None, description='ID тематики или подраздела тематики объявления.')
    category2_id: Optional[int] = Field(default=None, description='Дополнительная тематика.')
    status: Optional[int] = Field(
        default=None,
        description='Статус объявления. 0 — объявление остановлено; 1 — объявление запущено; 2 — объявление удалено.'
    )
    age_restriction: Optional[int] = Field(default=None, description='Возрастное ограничение.')
    name: Optional[str] = Field(default=None, description='Название объявления.')
    approved: Optional[int] = Field(default=None, description='Статус модерации объявления.')
    video: Optional[int] = Field(default=None, description='Объявление является видеорекламой.')
    disclaimer_medical: Optional[int] = Field(
        default=None,
        description='Включено отображение предупреждения: "Есть противопоказания. Требуется консультация специалиста".'
    )
    disclaimer_specialist: Optional[int] = Field(
        default=None,
        description='Включено отображение предупреждения: "Необходима консультация специалистов".'
    )
    disclaimer_supplements: Optional[int] = Field(
        default=None,
        description='Включено отображение предупреждения: "БАД. Не является лекарственным препаратом".'
    )
    create_time: Optional[int] = Field(default=None, description='Время создания.')
    update_time: Optional[int] = Field(default=None, description='Время последнего обновления.')
    start_time: Optional[int] = Field(default=None, description='Время начала показа объявления.')
    stop_time: Optional[int] = Field(default=None, description='Время окончания показа объявления.')
    publisher_platforms_auto: Optional[int] = Field(
        default=None,
        description='Автоматический выбор площадок для показа.'
    )
    has_campaign_budget_optimization: Optional[bool] = Field(default=None, description='Оптимизация бюджета кампании.')
    events_retargeting_groups: Optional[List[EventRetargetingGroup]] = Field(
        default=None,
        description='Группы ретаргетинга.'
    )


class AdLayoutSchema(__BaseSchema):
    """
    Модель описания внешнего вида рекламных объявлений.
    https://dev.vk.com/ru/method/ads.getAdsLayout
    """
    id: Optional[int] = Field(default=None, description='Идентификатор объявления.')
    campaign_id: Optional[int] = Field(default=None, description='Идентификатор кампании.')
    ad_format: Optional[int] = Field(default=None, description='Формат объявления.')
    cost_type: Optional[int] = Field(
        default=None,
        description='Тип оплаты. 0 — оплата за переходы; 1 — оплата за показы; 3 — оптимизированная оплата за показы.'
    )
    goal_type: Optional[int] = Field(
        default=None,
        description='Тип цели. Подробное описание: https://dev.vk.com/ru/method/ads/goals'
    )
    video: Optional[int] = Field(default=None, description='1 — Объявление является видеорекламой.')
    repeat_video: Optional[int] = Field(default=None, description='Зацикливание видео.')
    title: Optional[str] = Field(default=None, description='Заголовок объявления.')
    description: Optional[str] = Field(default=None, description='Описание объявления.')
    link_url: Optional[str] = Field(default=None, description='Ссылка на рекламируемый объект.')
    link_domain: Optional[str] = Field(default=None, description='Домен рекламируемого объекта.')
    link_title: Optional[str] = Field(default=None, description='Заголовок рядом с кнопкой или ссылкой.')
    link_button: Optional[str] = Field(default=None, description='Идентификатор кнопки объявления.')
    preview_link: Optional[str] = Field(default=None, description='Ссылка для просмотра рекламного объявления.')
    image_src: Optional[str] = Field(default=None, description='URL изображения объявления.')
    image_src_2x: Optional[str] = Field(default=None, description='URL изображения двойного разрешения.')
    icon_src: Optional[str] = Field(default=None, description='URL логотипа объявления.')
    icon_src_2x: Optional[str] = Field(default=None, description='URL логотипа двойного разрешения.')
    age_restriction: Optional[int] = Field(default=None, description='Возрастное ограничение.')
    link_type: Optional[int] = Field(default=None, description='Тип ссылки.')
    social: Optional[bool] = Field(default=None, description='Флаг социального объекта.')
    okved: Optional[str] = Field(default=None, description='ОКВЭД объекта рекламы.')
    hide_likes: Optional[bool] = Field(default=None, description='Скрытие отображения лайков.')
    new_publisher_platforms: Optional[bool] = Field(default=None, description='Новые платформы публикации.')


class StatisticSchema(__BaseSchema):
    """
    Модель статистики показателей эффективности.
    https://dev.vk.com/ru/method/ads.getStatistics
    """
    id: Optional[int] = Field(default=None, description='ID объекта из параметра ids.')
    type: Optional[str] = Field(default=None, description='Тип объекта из параметра ids_type.')
    stats: Optional[List[StatisticItemSchema]] = Field(
        default=None,
        description='Список структур описывающих статистику объекта.'
    )
