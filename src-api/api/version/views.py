from rest_framework.views import APIView
from rest_framework.response import Response

from jara.settings import VERSION


class VersionView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, _):
        return Response(data={'version': VERSION}, status=200)
