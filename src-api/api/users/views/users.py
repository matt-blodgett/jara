import datetime

from django.contrib.auth import hashers

from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from api.users import models as user_models


class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(allow_null=False, max_length=45, allow_blank=False)
    first_name = serializers.CharField(allow_null=True, max_length=45, allow_blank=False)
    last_name = serializers.CharField(allow_null=True, max_length=45, allow_blank=False)
    email = serializers.CharField(allow_null=True, max_length=128, allow_blank=False)
    password = serializers.CharField(allow_null=False, max_length=128, allow_blank=False, write_only=True)

    def create(self, validated_data):
        pwd_raw = validated_data['password']
        pwd_hashed = hashers.make_password(pwd_raw, salt=None)
        validated_data['password'] = pwd_hashed
        validated_data['dt_created'] = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance

    class Meta:
        model = user_models.User
        fields = [
            'user_id',
            'first_name',
            'last_name',
            'email',
            'password'
        ]


class UserViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSerializer
    queryset = user_models.User.objects
    lookup_field = 'user_id'
    lookup_url_kwarg = 'user_id'
