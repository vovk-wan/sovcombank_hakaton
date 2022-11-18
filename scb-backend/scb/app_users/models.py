"""
models.py
---------
Модуль описывает модели приложения app_users
"""
from django.contrib.auth.models import User
from django.db import models


class SubscriptionTypeModel(models.Model):
    name = models.CharField(max_length=250, verbose_name="Тип подписки")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "subscriptions_types"


class RoleModel(models.Model):
    name = models.CharField(max_length=250, verbose_name="Тип подписки")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "role"


class ProfileModel(models.Model):
    """class for storing additional information about users"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250, verbose_name="Адрес")
    gender = models.CharField(default=None, max_length=5, blank=True, null=True)
    birth_date = models.DateField(
        default=None, blank=True, null=True, verbose_name="Дата рождения"
    )
    birth_place = models.CharField(
        default=None, blank=True, null=True, verbose_name="Место рождения"
    )
    biography = models.TextField(
        default=None, blank=True, null=True, verbose_name="Биография"
    )
    subscription_type = models.ForeignKey(
        SubscriptionTypeModel,
        related_name="profile",
        on_delete=models.CASCADE,
        verbose_name="Тип подписки",
    )
    role = models.ForeignKey(
        RoleModel, related_name="profile", on_delete=models.CASCADE, verbose_name="Роль"
    )
    verification = models.BooleanField(default=False)
    published_blog = models.IntegerField(default=0)
    description = models.TextField(max_length=1000, default="", verbose_name="О себе")
    info = models.JSONField(default=None, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "profiles"
