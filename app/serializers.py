from rest_framework import serializers

from app.models import Customer, Device
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        )


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = (
            'id',
            'user',
            'description'
        )


class CustomerCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()

    class Meta:
        model = Customer
        fields = (
            'user_id',
            'description'
        )

    def create(self, validated_data):
        instance = super().create(validated_data)

        return instance


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = (
            'dev_eui',
            'state',
            'description',
            'last_reading_time',
            'activation_time',
            'description',
            'type',
            'owner'                                                    # uuid from Customer
        )
