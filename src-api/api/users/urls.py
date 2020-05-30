from django.urls import path

from api.users import views as user_views


urlpatterns = [
    path('authenticate', user_views.UserAuthenticationView.as_view()),
    path('users', user_views.UserViewSet.as_view(actions={'post': 'create'})),
    path('validate/users', user_views.UserValidationView.as_view())
]
