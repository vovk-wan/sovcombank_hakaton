"""
models.py
---------
Модуль описывает модели приложения app_users
"""
from django.contrib.auth.models import User
from django.db import models


class FirstCreateProfile:
    role = 30
    account_type = 10
    currency = "RUB"


class RoleCodes:
    admin = 10
    company = 20
    human = 30


class SubscriptionTypeModel(models.Model):
    """Модель типы подписок"""

    name = models.CharField(max_length=250, verbose_name="Тип подписки")
    default = models.BooleanField(verbose_name="по умолчанию", default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "subscription_types"
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"


class RoleModel(models.Model):
    """Модель ролей"""

    name = models.CharField(max_length=250, verbose_name="Роль пользователя")
    code = models.IntegerField(verbose_name="код роли", db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "roles"
        verbose_name = "Роль"
        verbose_name_plural = "Роли"


class ProfileModel(models.Model):
    """Модель расширение модели пользователей"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(
        max_length=250, verbose_name="Адрес", blank=True, null=True
    )
    gender = models.CharField(default=None, max_length=15, blank=True, null=True)
    birth_date = models.DateField(
        default=None, blank=True, null=True, verbose_name="Дата рождения"
    )
    birth_place = models.CharField(
        max_length=250,
        default=None,
        blank=True,
        null=True,
        verbose_name="Место рождения",
    )
    biography = models.TextField(
        default=None, blank=True, null=True, verbose_name="Биография"
    )
    subscription_type = models.ForeignKey(
        SubscriptionTypeModel,
        related_name="profile",
        on_delete=models.PROTECT,
        verbose_name="Тип подписки",
    )
    role = models.ForeignKey(
        RoleModel, related_name="profile", on_delete=models.PROTECT, verbose_name="Роль"
    )
    verification = models.BooleanField(default=False)
    published_blog = models.IntegerField(default=0)
    info = models.JSONField(default=None, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "profiles"
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
