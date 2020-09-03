from rest_framework.views import APIView
from rest_framework.response import Response

from jara.settings import JARA_VERSION


class VersionView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, _):
        return Response(data={'version': JARA_VERSION}, status=200)
