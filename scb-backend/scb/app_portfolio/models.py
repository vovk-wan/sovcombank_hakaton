"""
models.py
---------
Модели приложения Портфель
"""
from django.db import models

from app_transaction.models import TransactionModel
from app_users.models import ProfileModel


class RewardStatusModel(models.Model):
    """
    Статус поощрения
    """

    name = models.CharField(max_length=255, verbose_name="название")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "reward_statuses"
        verbose_name = "Статус награды"
        verbose_name_plural = "Статусы наград"


class CurrencyModel(models.Model):
    """
    Модель валюты
    """

    name = models.CharField(max_length=255, verbose_name="название")
    description = models.TextField(verbose_name="описание")

    class Meta:
        db_table = "currencies"


class RewardModel(models.Model):
    """
    модель системы поощрений
    """

    name = models.CharField(max_length=255, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    status = models.ForeignKey(
        RewardStatusModel, on_delete=models.PROTECT, related_name=""
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "rewards"
        verbose_name = "Награда"
        verbose_name_plural = "Награды"


class PortfolioModel(models.Model):
    """
    Модель портфеля
    """

    name = models.CharField(max_length=255, verbose_name="название")
    profile = models.ForeignKey(
        ProfileModel,
        on_delete=models.PROTECT,
        related_name="portfolio",
        verbose_name="профиль",
    )
    price = models.DecimalField(verbose_name="цена", db_index=True)
    encouragement = models.ForeignKey(
        RewardModel,
        on_delete=models.PROTECT,
        related_name="portfolios",
        verbose_name="поощрение",
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "portfolio"
        verbose_name = "Портфель"
        verbose_name_plural = "Портфели"


class InstrumentTypeModel(models.Model):
    """
    Тип инструментов
    """

    name = models.CharField(max_length=255, verbose_name="Тип инструмента")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "instrument_types"
        verbose_name = "тип инструмента"
        verbose_name_plural = "типы инструментов"


class InstrumentModel(models.Model):
    """
    Модель финансовых инструментов.
    """

    name = models.CharField(max_length=255, verbose_name="название")
    instrument_type = models.ForeignKey(
        InstrumentTypeModel,
        on_delete=models.PROTECT,
        related_name="instruments",
        verbose_name="тип инструмента",
    )
    icon = models.ImageField(verbose_name="иконка инструмента")
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "instruments"
        verbose_name = "Инструмент"
        verbose_name_plural = "Инструменты"


class FavoriteModel(models.Model):
    """
    Модель избранных инструментов
    """

    profile = models.ForeignKey(
        ProfileModel,
        on_delete=models.PROTECT,
        related_name="profile",
        verbose_name="профиль",
    )
    instrument = models.ForeignKey(
        InstrumentModel,
        on_delete=models.PROTECT,
        related_name="favorites",
        verbose_name="инструмент",
    )

    class Meta:
        db_table = "favorites"


class AccountTypeModel(models.Model):
    """
    Модель типов счетов
    """

    name = models.CharField(max_length=255, verbose_name="название")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "account_types"
        verbose_name = "Тип счета"
        verbose_name_plural = "Типы счетов"


class AccountModel(models.Model):
    """
    Модель счетов
    """

    name = models.CharField(max_length=255, verbose_name="название")
    portfolio = models.ForeignKey(
        PortfolioModel,
        on_delete=models.PROTECT,
        related_name="accounts",
        verbose_name="портфель",
    )
    account_type = models.ForeignKey(
        AccountTypeModel,
        on_delete=models.PROTECT,
        related_name="accounts",
        verbose_name="тип счета",
    )
    current_curency = models.ForeignKey(
        CurrencyModel,
        on_delete=models.PROTECT,
        related_name="current_curencys",
        verbose_name="текущая валюта",
    )
    transaction = models.ForeignKey(
        TransactionModel,
        on_delete=models.PROTECT,
        related_name="accounts",
        verbose_name="транзакция",
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "accounts"
        verbose_name = "Счёт"
        verbose_name_plural = "Счета"
