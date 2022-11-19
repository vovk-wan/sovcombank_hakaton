from django.contrib import admin

from app_transaction.models import TransactionModel, TransactionTypeModel


@admin.register(TransactionModel)
class TransactionAdmin(admin.ModelAdmin):
    """
    Регистрация в административной панели
    """

    search_fields = ["created_at"]
    raw_id_fields = ("profile",)


@admin.register(TransactionTypeModel)
class TransactionTypeAdmin(admin.ModelAdmin):
    """
    Регистрация в административной панели
    """

    search_fields = ["name"]
