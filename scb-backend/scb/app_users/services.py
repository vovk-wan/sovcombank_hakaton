"""
services.py
-----------
Модуль описывает бизнес-логику приложения app_users
"""
from django.contrib.auth.models import User

from app_users.models import ProfileModel, RoleCodes, RoleModel, SubscriptionTypeModel
from app_users.serialisers import RegisterInSerialiser, RegisterOutSerializer


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
        if data.get("role") == "admin":
            role = RoleModel.objects.get(code=RoleCodes.admin)
        elif data.get("role") == "company":
            role = RoleModel.objects.get(code=RoleCodes.company)
        else:
            role = RoleModel.objects.get(code=RoleCodes.human)
        subscribe = SubscriptionTypeModel.objects.get(default=True)
        if not subscribe:
            raise ValueError("нет подписки по умолчанию")
        ProfileModel.objects.create(user=user, role=role, subscription_type=subscribe)
