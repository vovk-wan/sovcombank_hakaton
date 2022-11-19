from django.contrib import admin

from app_portfolio.models import (
    AccountModel,
    AccountTypeModel,
    CurrencyModel,
    FavoriteModel,
    InstrumentModel,
    InstrumentTypeModel,
    PortfolioModel,
    RewardModel,
    RewardStatusModel,
)


@admin.register(PortfolioModel)
class PortfolioAdmin(admin.ModelAdmin):
    """Регистрация в административной панели моделей"""

    search_fields = ["name"]
    raw_id_fields = ("profile",)


@admin.register(CurrencyModel)
class CurrencyAdmin(admin.ModelAdmin):
    """Регистрация в административной панели моделей"""

    search_fields = ["name"]


@admin.register(InstrumentModel)
class InstrumentAdmin(admin.ModelAdmin):
    """Регистрация в административной панели моделей"""

    search_fields = ["name"]


@admin.register(RewardModel)
class RewardAdmin(admin.ModelAdmin):
    """Регистрация в административной панели моделей"""

    search_fields = ["name"]


@admin.register(AccountTypeModel)
class AccountTypeAdmin(admin.ModelAdmin):
    """Регистрация в административной панели моделей"""

    search_fields = ["name"]


@admin.register(RewardStatusModel)
class RewardStatusAdmin(admin.ModelAdmin):
    """Регистрация в административной панели моделей"""

    search_fields = ["name"]


@admin.register(InstrumentTypeModel)
class InstrumentTypeAdmin(admin.ModelAdmin):
    """Регистрация в административной панели моделей"""

    search_fields = ["name"]


@admin.register(FavoriteModel)
class FavoriteAdmin(admin.ModelAdmin):
    """Регистрация в административной панели моделей"""

    raw_id_fields = ("profile",)


@admin.register(AccountModel)
class AccountAdmin(admin.ModelAdmin):
    """Регистрация в административной панели моделей"""

    search_fields = ["name"]
    raw_id_fields = ("portfolio", "transaction")
