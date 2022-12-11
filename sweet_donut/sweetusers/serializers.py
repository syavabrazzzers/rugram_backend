from rest_framework.serializers import Serializer, ModelSerializer
from django.contrib.auth import get_user_model
from django.db import models, IntegrityError
from .models import Profile
from django.contrib.auth.models import AbstractUser
from djoser.serializers import UserCreateSerializer as DjoserCreateUserSerializer
from djoser.serializers import UserSerializer as DjoserUserSerializer
from djoser import serializers

User = get_user_model()


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password',
        )


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'is_active',
            'last_login'
        )


class UserProfileSerializer(DjoserUserSerializer):

    user = UserSerializer(required=True)

    class Meta(DjoserUserSerializer.Meta):
        model = Profile
        fields = '__all__'


class UserCreateSerializer(DjoserCreateUserSerializer):
    class Meta(DjoserCreateUserSerializer.Meta):
        model = User
        fields = (
            'username',
            'email',
            'password'
        )

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")
        profile = Profile(user=user)
        profile.save()
        print('CREATE FROM CUSTOM')
        return user