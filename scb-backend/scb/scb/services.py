"""
services.py
-----------
Модуль содержит бизнес-логику приложения
"""
from django.core.cache import cache
from django.http.request import HttpRequest
from loguru import logger

from .tasks import get_data_from_api

url = (
    "https://www.alphavantage.co/query?"
    "function={FUNCTION}"
    "symbol={SYMBOL}"
    "interval={INTERVAL}"
    "apikey={APIKEY}"
)


class ApiDataService:
    """Класс реализует получение данных по определённым параметрам"""

    @classmethod
    def check_cache(cls, request, *args, **kwargs):
        user = request.user
        key = f"{user}::TIME_SERIES_INTRADAY"
        logger.info(key)
        if result := cache.get(key):
            logger.info(f"return data from cache")
            return result
        logger.info("start celery task...")
        get_data_from_api.delay(config=dict(key=key))
