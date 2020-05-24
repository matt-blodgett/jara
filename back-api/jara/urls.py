from django.urls import path

from api.version.views import VersionView


urlpatterns = [
    path('api/version', VersionView.as_view())
]
