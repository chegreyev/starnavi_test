from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User


class UserShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'uuid',
            'full_name',
        )


class UserRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'uuid',
            'email',
            'first_name',
            'last_name',
            'patronymic',
            'phone',
            'last_activity',
            'last_login',
        )


class UserCreateSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(label='Confirm password', write_only=True)

    class Meta:
        model = User
        fields = (
            'created_at',
            'updated_at',
            'uuid',
            'email',
            'first_name',
            'last_name',
            'phone',
            'password',
            'confirm_password'
        )

        extra_kwargs = {
            'uuid': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.pop('confirm_password')
        if password != confirm_password:
            raise ValidationError({'password': ['passwords are not equal.']})
        return attrs

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'created_at',
            'updated_at',
            'uuid',
            'email',
            'first_name',
            'last_name',
            'phone',
            'password'
        )

    def update(self, instance: User, validated_data):
        if validated_data.get('password', None):
            instance.set_password(validated_data['password'])
        return super().update(instance, validated_data)
