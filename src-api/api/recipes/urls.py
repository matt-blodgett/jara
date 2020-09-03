from django.urls import path

from api.recipes import views as recipe_views


urlpatterns = [
    path('recipes', recipe_views.RecipeViewSet.as_view(actions={'post': 'create'}))
]
