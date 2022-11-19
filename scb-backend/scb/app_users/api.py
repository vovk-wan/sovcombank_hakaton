"""
api.py
------
Модуль реализует апи-представления для приложения app_users
"""
from django.db import transaction
from django.db.utils import IntegrityError
from drf_spectacular.utils import extend_schema
from loguru import logger
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView

from app_users.models import ProfileModel
from app_users.serializers import (
    ProfileOutSerializer,
    RegisterInSerialiser,
    RegisterOutSerializer,
)
from app_users.services import RegisterService


class RegistrationApiView(APIView):
    """
    Api-представление регистрации нового пользователя
    """

    @extend_schema(
        request=RegisterInSerialiser, responses=RegisterOutSerializer, auth=None
    )
    def post(self, request):
        """
        метод регистрирует пользователя
        :param request:
        :return:
        """
        data = RegisterInSerialiser(data=request.data)
        try:
            if not data.is_valid():
                return Response(
                    dict(error="Ошибка валидации"), status=status.HTTP_403_FORBIDDEN
                )
            with transaction.atomic():
                if response := RegisterService().register(serializer=data):
                    return Response(response.data)
        except IntegrityError as e:
            logger.exception(e)
            return Response(
                dict(error="непредвиденная ошибка"),
                status=status.HTTP_403_FORBIDDEN,
            )
        except ValidationError as e:
            logger.exception(e)
            return Response(
                dict(error="ошибка валидации", data=data.errors),
                status=status.HTTP_403_FORBIDDEN,
            )
        except ValueError as e:
            logger.exception(e)
            return Response(
                dict(error="ошибка", data=data.errors),
                status=status.HTTP_403_FORBIDDEN,
            )


class ProfileListApiView(APIView):
    """api представление для вывода всех профилей"""

    def get(self, request, format=None):
        """получим список профилей для авторизованного юзера"""
        profiles = (
            ProfileModel.objects.select_related("user")
            .prefetch_related(
                "portfolios__accounts__account_type",
                "portfolios__accounts__current_currency",
            )
            .filter(user=self.request.user)
        )
        serializer = ProfileOutSerializer(profiles, many=True)
        return Response(serializer.data)
