from rest_framework import serializers

from app.models import Customer, Device
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


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

    def create(self, validated_data):
        password = validated_data.get('password')
        hashed_password = make_password(password)
        validated_data['password'] = hashed_password
        instance = super(UserSerializer, self).create(validated_data)
        return instance


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'description',
        )


class CustomerFullSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = (
            'user',
            'description',
        )


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = (
            'uuid',
            'dev_eui',
            'state',
            'description',
            'last_reading_time',
            'activation_time',
            'description',
            'type',
            'owner'  # uuid from Customer
        )


class DeviceCSVSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = (
            'description',
        )


class SuccessSerializer(serializers.Serializer):
    success = serializers.BooleanField()
