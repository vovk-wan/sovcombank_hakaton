from rest_framework import serializers

from app_users.models import ProfileModel, SubscriptionTypeModel


class RegisterInSerialiser(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField()


class RegisterOutSerializer(serializers.Serializer):
    status = serializers.CharField()
    login = serializers.CharField()


class ProfileOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        exclude = ["user"]
        depth = 1
