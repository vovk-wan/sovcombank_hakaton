from rest_framework import serializers

from app_users.models import ProfileModel, SubscriptionTypeModel


class RegisterInSerialiser(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField()


class RegisterOutSerializer(serializers.Serializer):
    status = serializers.CharField()
    login = serializers.CharField()


class SubscribtionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionTypeModel
        fields = "__all__"


class ProfileOutSerializer(serializers.ModelSerializer):

    subscription_type = SubscribtionTypeSerializer()

    class Meta:
        model = ProfileModel
        fields = "__all__"
        depth = 1
