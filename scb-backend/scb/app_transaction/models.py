"""
models.py
---------
модуль определяет модели приложения транзакций
"""
from django.db import models

from app_portfolio.models import InstrumentModel


class TransactionTypeModel(models.Model):
    """
    Тип инструментов
    """

    name = models.CharField(max_length=255, verbose_name="Типы транзакций")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "тип транзакций"
        verbose_name_plural = "типы транзакций"


class TransactionModel(models.Model):
    """
    модель транзакций
    """

    profile = models.ForeignKey(
        "ProfileModel",
        on_delete=models.PROTECT,
        related_name="profile",
        verbose_name="профиль",
    )
    instrument = models.ForeignKey(
        InstrumentModel,
        on_delete=models.PROTECT,
        related_name="transactions",
        verbose_name="инструмент",
    )
    transaction_type = models.ForeignKey(
        TransactionTypeModel,
        on_delete=models.PROTECT,
        related_name="transactions",
        verbose_name="тип транзакций",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name="Время транзакции"
    )
    price = models.DecimalField(verbose_name="сумма транзакции", db_index=True)

    def __str__(self):
        return self.transaction_type.name

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"
