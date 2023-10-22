from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from api.users import models as user_models


class RequestSerializer(serializers.Serializer):
    username = serializers.CharField()


class UserCheckExistsView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        query_params = RequestSerializer(data=request.query_params)
        query_params.is_valid(raise_exception=True)
        query_params = query_params.validated_data

        exists = user_models.User.objects.filter(
            username=query_params['username']
        ).exists()

        data = {
            'exists': exists
        }
        return Response(data=data, status=200)
