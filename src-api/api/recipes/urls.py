from django.urls import path

from api.recipes.views import RecipeViewSet


urlpatterns = [
    path('recipes', RecipeViewSet.as_view(actions={'post': 'create', 'get': 'list'})),
    path('recipes/<int:id>', RecipeViewSet.as_view(actions={'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]
