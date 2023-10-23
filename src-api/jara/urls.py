from django.urls import path
from django.urls import include


urlpatterns = [
    path('api/', include('api.version.urls')),
    path('api/users/', include('api.users.urls')),
    path('api/recipes/', include('api.recipes.urls'))
]
