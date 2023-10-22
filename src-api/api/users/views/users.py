from django.contrib.auth import hashers

from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from api.users import models as user_models


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30, min_length=3)
    password = serializers.CharField(max_length=128, write_only=True)
    email = serializers.EmailField(max_length=128)

    def create(self, validated_data):
        pwd_raw = validated_data['password']
        pwd_hashed = hashers.make_password(pwd_raw, salt=None)
        validated_data['password'] = pwd_hashed
        instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance

    class Meta:
        model = user_models.User
        fields = [
            'username',
            'password',
            'email'
        ]


class UserViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSerializer
    queryset = user_models.User.objects.all()
    lookup_field = 'username'
    lookup_url_kwarg = 'username'
