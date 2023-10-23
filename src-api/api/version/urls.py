from django.urls import path

from api.version.views import VersionView


urlpatterns = [
    path('version', VersionView.as_view())
]
