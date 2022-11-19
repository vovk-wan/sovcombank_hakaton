"""
services.py
-----------
Модуль содержит бизнес-логику приложения app_portfolio
"""
from app_portfolio.models import (
    AccountModel,
    AccountTypeModel,
    CurrencyModel,
    PortfolioModel,
)
from app_users.models import ProfileModel


class PortfolioService:
    """сервис управления портфелями"""

    def create(self, profile: ProfileModel):
        portfolio = PortfolioModel.objects.create(
            name="Новый портфель",
            profile=profile,
        )
        return portfolio


class AccountService:
    """
    сервис управления счетами
    """

    def create(
        self,
        portfolio: PortfolioModel,
        acc_type: AccountTypeModel,
        currency: CurrencyModel,
    ):
        account = AccountModel.objects.create(
            name="Новый счет",
            portfolio=portfolio,
            account_type=acc_type,
            current_currency=currency,
        )
        if not account:
            raise ValueError("не удалось создать счет")
        return account
