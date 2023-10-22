from django.urls import path
from django.urls import include

from api.version.views import VersionView


urlpatterns = [
    path('api/version', VersionView.as_view()),
    path('api/users/', include('api.users.urls'))
]
