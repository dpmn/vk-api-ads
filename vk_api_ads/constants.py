class IDType(object):
    """
    Тип запрашиваемых объектов.
    """
    AD = 'ad'  # объявления
    CAMPAIGN = 'campaign'  # кампании
    CLIENT = 'client'  # клиенты
    OFFICE = 'office'  # кабинет


class StatisticsPeriod(object):
    """
    Способ группировки данных по датам.
    """
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    YEAR = 'year'
    OVERALL = 'overall'  # статистика за всё время
