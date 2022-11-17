import requests
from django.core.cache import cache
from loguru import logger

from .celery import app

TASK_CACHE_TIMEOUT = 600000


@app.task(bind=True)
def get_data_from_api(backend_response, config: dict):
    logger.warning("celery is running")
    url = (
        r"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY"
        r"&symbol=IBM&interval=5min&apikey=demo"
    )
    if "key" not in config.keys():
        logger.error("key not found")
        return
    logger.warning(f"goto url: {url}")
    r = requests.get(url)
    key = config["key"]
    if r.status_code == 200:
        data = r.json()
        cache.set(key, data, TASK_CACHE_TIMEOUT)
        logger.info(f"set result to key: {key}")
    else:
        logger.error(f"{r.status_code}")
