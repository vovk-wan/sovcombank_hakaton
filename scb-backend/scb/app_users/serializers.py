from django.contrib.auth.models import User
from rest_framework import serializers

from app_portfolio.serializers import PortfolioOutSerializer
from app_users.models import ProfileModel


class RegisterInSerialiser(serializers.Serializer):
    """входная схема учетных данных регистрации пользователя"""

    login = serializers.CharField()
    password = serializers.CharField()


class RegisterOutSerializer(serializers.Serializer):
    """выходная схема регистрации пользователя"""

    status = serializers.CharField()
    login = serializers.CharField()


class UserOutSerializer(serializers.ModelSerializer):
    """сериализация пользователя для профиля"""

    class Meta:
        model = User
        exclude = ("password",)


class ProfileOutSerializer(serializers.ModelSerializer):
    """сериализация модели пользователя и всего остального"""

    user = UserOutSerializer(read_only=True)
    portfolios = PortfolioOutSerializer(many=True, read_only=True)

    class Meta:
        model = ProfileModel
        fields = "__all__"
        depth = 1
