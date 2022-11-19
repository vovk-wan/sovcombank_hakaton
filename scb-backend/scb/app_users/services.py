"""
services.py
-----------
Модуль описывает бизнес-логику приложения app_users
"""
from django.contrib.auth.models import User

from app_portfolio.models import AccountTypeModel, CurrencyModel, PortfolioModel
from app_portfolio.services import AccountService, PortfolioService
from app_users.models import (
    FirstCreateProfile,
    ProfileModel,
    RoleCodes,
    RoleModel,
    SubscriptionTypeModel,
)
from app_users.serializers import RegisterInSerialiser, RegisterOutSerializer


class RegisterService:
    """
    Сервис регистрации нового пользователя
    """

    def register(self, serializer: RegisterInSerialiser) -> RegisterOutSerializer:
        """метор создаёт нового пользователя"""
        user = User.objects.create_user(
            username=serializer.validated_data.get("login"),
            email=serializer.validated_data.get("login"),
            password=serializer.validated_data.get("password"),
            is_active=False,
        )
        user.save()
        ProfileService().create(
            user, data=dict(role=serializer.validated_data.get("role", "human"))
        )
        response = RegisterOutSerializer(
            data=dict(status="регистрация прошла успешно", login=user.username)
        )
        if response.is_valid():
            return response


class ProfileService:
    """сервис профилей пользователей"""

    def create(self, user: User, data: dict):
        subscribe = self._create_subsctibe()
        role = self._get_role(data)
        profile = ProfileModel.objects.create(
            user=user, role=role, subscription_type=subscribe
        )
        portfolio = self._create_portfolio(profile)
        self._create_account(portfolio, currency_name=FirstCreateProfile.currency)

    def _get_role(self, data: dict) -> RoleModel:
        """получим роль"""
        if data.get("role") == "admin":
            role = RoleModel.objects.get(code=RoleCodes.admin)
        elif data.get("role") == "company":
            role = RoleModel.objects.get(code=RoleCodes.company)
        else:
            role = RoleModel.objects.get(code=RoleCodes.human)
        if not role:
            raise ValueError("нет подходящей роли")
        return role

    def _create_subsctibe(self):
        """получим подписку"""
        subscribe = SubscriptionTypeModel.objects.get(default=True)
        if not subscribe:
            raise ValueError("нет подписки по умолчанию")
        return subscribe

    def _create_portfolio(self, profile: ProfileModel):
        portfolio = PortfolioService().create(profile=profile)
        if not portfolio:
            raise ValueError("не удалось создать новый портфель")
        return portfolio

    def _create_account(self, portfolio: PortfolioModel, currency_name: str):
        """создаём счёт"""
        acc_type = AccountTypeModel.objects.get(code=FirstCreateProfile.account_type)
        if not acc_type:
            raise ValueError("не удалось найти тип счета")
        currency = CurrencyModel.objects.get(name=currency_name)
        if not currency:
            raise ValueError(f"не удалось найти подходящую валюту {currency_name}")
        account = AccountService().create(
            portfolio=portfolio, acc_type=acc_type, currency=currency
        )
        return account
