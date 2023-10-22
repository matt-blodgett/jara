import datetime

import jwt
from django.contrib.auth import hashers

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from jara.settings import SECRET_KEY
from api.users import models as user_models


TOKEN_EXPIRY_SECONDS = 60 * 60 * 24


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    timestamp = serializers.SerializerMethodField()
    expiry = serializers.SerializerMethodField()

    def get_timestamp(self, _):
        now = datetime.datetime.now()
        return now.strftime('%Y-%m-%dT%H:%M:%SZ')

    def get_expiry(self, _):
        now = datetime.datetime.now()
        td = datetime.timedelta(seconds=TOKEN_EXPIRY_SECONDS)
        return (now + td).timestamp()

    class Meta:
        model = user_models.User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'timestamp',
            'expiry'
        ]


def authenticate(username, password):
    token = None
    profile = None

    try:
        user = user_models.User.objects.get(username=username)
    except user_models.User.DoesNotExist:
        user = None

    if user and hashers.check_password(password, user.password):
        profile = ProfileSerializer(user).data
        token = jwt.encode(profile, SECRET_KEY, algorithm='HS256').decode(encoding='UTF-8')

    return token, profile


class RequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserAuthenticationView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        post_data = RequestSerializer(data=request.data)
        post_data.is_valid(raise_exception=True)
        post_data = post_data.validated_data

        token, profile = authenticate(post_data['username'], post_data['password'])
        if not token or not profile:
            return Response(data={}, status=401)

        data = {
            'token': token,
            'profile': profile
        }
        return Response(data=data, status=200)
