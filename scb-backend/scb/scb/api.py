# https://www.alphavantage.co/support/#api-key
# Welcome to Alpha Vantage! Here is your API key: XJ7NTHIG2UR6Y8BI. Please record this API key at a safe place for future data access.

# https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
# https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=1min&apikey=demo
# outputsize=compact

# https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=demo
# https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tesco&apikey=demo
# import requests
#
# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
# r = requests.get(url)
# data = r.json()
#
# print(data)
from loguru import logger
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import ApiDataService


class TestView(APIView):
    def post(self, request, *args, **kwargs):
        return Response(
            {"name": "vovk", "status": "good man"}, status=status.HTTP_201_CREATED
        )


class ExampleApiQuery(APIView):
    def get(self, request, *args, **kwargs):
        logger.info("run api")
        ApiDataService.check_cache(request)
        return Response(dict(status="OK"), status=status.HTTP_200_OK)
