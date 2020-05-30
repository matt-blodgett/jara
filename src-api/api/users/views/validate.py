from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from api.users import models as user_models


class RequestSerializer(serializers.Serializer):
    user_id = serializers.CharField()


class UserValidationView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        query_params = RequestSerializer(data=request.query_params)
        query_params.is_valid(raise_exception=True)
        query_params = query_params.validated_data

        if user_models.User.objects.filter(user_id=query_params['user_id']).exists():
            raise serializers.ValidationError(detail='user_id exists')

        data = {'valid': True}
        return Response(data=data, status=200)
