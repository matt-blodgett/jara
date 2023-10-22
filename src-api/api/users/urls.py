from django.urls import path

from api.users.views.authenticate import UserAuthenticationView
from api.users.views.users import UserViewSet
from api.users.views.check_exists import UserCheckExistsView


urlpatterns = [
    path('auth', UserAuthenticationView.as_view()),
    path('users', UserViewSet.as_view(actions={'post': 'create'})),
    path('check_exists', UserCheckExistsView.as_view())
]
