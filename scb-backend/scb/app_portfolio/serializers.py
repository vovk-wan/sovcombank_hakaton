"""
serializers.py
--------------
Модуль содержит сериализаторы приложения app_portfolio
"""
from rest_framework import serializers

from app_portfolio.models import AccountModel, PortfolioModel


class AccountOutSerializer(serializers.ModelSerializer):
    """Сериализация счета"""

    class Meta:
        model = AccountModel
        depth = 1
        exclude = ["transaction", "portfolio"]


class PortfolioOutSerializer(serializers.ModelSerializer):
    """сериализация портфеля"""

    accounts = AccountOutSerializer(many=True, read_only=True)

    class Meta:
        model = PortfolioModel
        depth = 1
        fields = "__all__"
