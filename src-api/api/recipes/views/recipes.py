import datetime

from django.contrib.auth import hashers

from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from api.recipes import models as recipe_models


class Recipe(JaraModel):
    created_by = models.CharField(null=False, blank=False, max_length=45)
    guid = models.CharField(null=False, blank=False, max_length=128)
    title = models.CharField(null=False, blank=False, max_length=45)
    description = models.TextField(null=True, blank=False, default=None)


class Instruction(JaraModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    index = models.IntegerField(null=False)
    text = models.TextField(null=False, blank=False)


class Ingredient(JaraModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    index = models.IntegerField(null=False)
    text = models.TextField(null=False, blank=False)


class IngredientSerializer(serializers.ModelSerializer):
    index = serializers.IntegerField()


class RecipeSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(allow_null=False, max_length=45, allow_blank=False)
    first_name = serializers.CharField(allow_null=True, max_length=45, allow_blank=False)
    last_name = serializers.CharField(allow_null=True, max_length=45, allow_blank=False)
    email = serializers.CharField(allow_null=True, max_length=128, allow_blank=False)
    password = serializers.CharField(allow_null=False, max_length=128, allow_blank=False, write_only=True)

    app_access = AppAccessSerializer(source='appaccess_set', many=True)
    equipment = AssetSerializer(source='asset_set', many=True)

    def create(self, validated_data):
        pwd_raw = validated_data['password']
        pwd_hashed = hashers.make_password(pwd_raw, salt=None)
        validated_data['password'] = pwd_hashed
        validated_data['created_at'] = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance

    class Meta:
        model = recipe_models.Recipe
        fields = [
            'user_id',
            'first_name',
            'last_name',
            'email',
            'password'
        ]


class RecipeViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSerializer
    queryset = user_models.User.objects
    lookup_field = 'user_id'
    lookup_url_kwarg = 'user_id'
