from django.db import models

from app_portfolio.models import RewardModel
from app_users.models import ProfileModel


class AchievementModel(models.Model):
    """Модель "достижения" """

    name = models.CharField(max_length=250, verbose_name="Название достижения")
    text = models.CharField(max_length=250, verbose_name="Текст")
    status = models.CharField(max_length=250, verbose_name="Статус")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "achievements"
        verbose_name = "Достижение профиля"
        verbose_name_plural = "Достижения профиля"


class AchievementProfileModel(models.Model):
    """Модель связи достижений с профилем"""

    achievement = models.ForeignKey(
        AchievementModel,
        related_name="achievement_profile",
        on_delete=models.CASCADE,
        verbose_name="Достижение",
    )
    is_achieve = models.BooleanField(default=False, verbose_name="Достижение получено")

    def __str__(self):
        return self.achievement.name

    class Meta:
        db_table = "achievements_profiles"
        verbose_name = "Достижение профиля"
        verbose_name_plural = "Достижения профилей"


class TituleProfileModel(models.Model):
    """Модель титул профиля TODO title?"""

    name = models.CharField(max_length=250, verbose_name="Титул")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "titule_profile"
        verbose_name = "Титул"
        verbose_name_plural = "Титулы"


class ExampleModel(models.Model):
    """TODO Что это"""

    name = models.CharField(max_length=250, verbose_name="Задание")
    text = models.CharField(max_length=250, verbose_name="Текст")
    status = models.CharField(max_length=250, verbose_name="Статус")
    description = models.TextField(verbose_name="Описание")
    reward = models.ForeignKey(
        RewardModel,
        related_name="examples",
        on_delete=models.PROTECT,
        verbose_name="Награды",
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "examples"
        verbose_name = "Задание"
        verbose_name_plural = "Задания"


class ExampleProfileModel(models.Model):
    """Модель связи достижений с профилем"""

    example = models.ForeignKey(
        ExampleModel,
        related_name="example_profile",
        on_delete=models.CASCADE,
        verbose_name="Задание",
    )
    is_achieve = models.BooleanField(default=False, verbose_name="Задание выполнено")

    def __str__(self):
        return self.example.name

    class Meta:
        db_table = "examples_profiles"
        verbose_name = "Задание профиля"
        verbose_name_plural = "Задания профилей"


class GamificationModel(models.Model):
    """Модель геймификации"""

    profile = models.OneToOneField(
        ProfileModel,
        related_name="gamification",
        on_delete=models.CASCADE,
        verbose_name="Профиль",
    )
    achievements_profile = models.ForeignKey(
        AchievementProfileModel, related_name="gamification", on_delete=models.PROTECT
    )
    titule_profile = models.OneToOneField(
        TituleProfileModel,
        related_name="gamification",
        on_delete=models.PROTECT,
        verbose_name="Титул",
    )
    example_profile = models.ForeignKey(
        ExampleModel,
        related_name="gamification",
        on_delete=models.PROTECT,
        verbose_name="Задание",
    )

    def __str__(self):
        return self.profile.user.username

    class Meta:
        db_table = "gamification"
        verbose_name = "Геймификация"
        verbose_name_plural = "Геймификация"
