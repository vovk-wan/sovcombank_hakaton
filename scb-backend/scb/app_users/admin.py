from django.contrib import admin

from app_users.models import ProfileModel, RoleModel, SubscriptionTypeModel


@admin.register(RoleModel)
class RoleAdmin(admin.ModelAdmin):
    """Регистрация в административной панели"""

    search_fields = ["name"]


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    """Регистрация в административной панели"""

    search_fields = ["user__username"]
    list_select_related = ["user"]
    raw_id_fields = ("user",)


@admin.register(SubscriptionTypeModel)
class SubscriptionTypeAdmin(admin.ModelAdmin):
    """Регистрация в административной панели"""

    search_fields = ["name"]
