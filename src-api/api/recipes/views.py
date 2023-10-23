from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from api.library.permissions import TokenPermission

from api.users import models as user_models
from api.recipes import models as recipe_models


class RecipeIngredientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    quantity = serializers.DecimalField(max_digits=8, decimal_places=2)
    unit_of_measure = serializers.CharField(max_length=32)
    name = serializers.CharField(max_length=100)

    class Meta:
        model = recipe_models.RecipeIngredient
        fields = [
            'id',
            'quantity',
            'unit_of_measure',
            'name'
        ]


class RecipeInstructionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(max_length=1024)

    class Meta:
        model = recipe_models.RecipeInstruction
        fields = [
            'id',
            'text'
        ]


class RecipeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=2048, allow_null=True, allow_blank=True, default=None)
    notes = serializers.CharField(max_length=4096, allow_null=True, allow_blank=True, default=None)

    ingredients = RecipeIngredientSerializer(source='recipeingredient_set', many=True)
    instructions = RecipeInstructionSerializer(source='recipeinstruction_set', many=True)

    created_by = serializers.CharField(read_only=True, source='created_by.username')
    created_at = serializers.DateTimeField(read_only=True)
    modified_at = serializers.DateTimeField(read_only=True)

    def create_nested_objects(self, instance, recipeingredient_set, recipeinstruction_set):
        recipeingredient_objects = []

        for obj in recipeingredient_set:
            recipeingredient_objects.append(recipe_models.RecipeIngredient(recipe=instance, **obj))

        recipeinstruction_objects = []

        for obj in recipeinstruction_set:
            recipeinstruction_objects.append(recipe_models.RecipeInstruction(recipe=instance, **obj))

        recipe_models.RecipeIngredient.objects.bulk_create(recipeingredient_objects, batch_size=50)
        recipe_models.RecipeInstruction.objects.bulk_create(recipeinstruction_objects, batch_size=50)

    def create(self, validated_data):
        username = self.context['request'].user['username']

        try:
            user_instance = user_models.User.objects.get(username=username)
        except user_models.DoesNotExist:
            raise serializers.ValidationError(detail=f'user not found {username}')

        validated_data['created_by'] = user_instance

        recipeingredient_set = validated_data.pop('recipeingredient_set')
        recipeinstruction_set = validated_data.pop('recipeinstruction_set')

        instance = super().create(validated_data)

        self.create_nested_objects(instance, recipeingredient_set, recipeinstruction_set)

        return instance

    def update(self, instance, validated_data):
        recipeingredient_set = validated_data.pop('recipeingredient_set')
        recipeinstruction_set = validated_data.pop('recipeinstruction_set')

        instance = super().update(instance, validated_data)

        instance.recipeingredient_set.all().delete()
        instance.recipeinstruction_set.all().delete()

        self.create_nested_objects(instance, recipeingredient_set, recipeinstruction_set)

        return instance

    class Meta:
        model = recipe_models.Recipe
        fields = [
            'id',
            'title',
            'description',
            'notes',
            'ingredients',
            'instructions',
            'created_by',
            'created_at',
            'modified_at'
        ]


class RecipeListSerializer(RecipeSerializer):

    class Meta:
        model = recipe_models.Recipe
        fields = [
            'id',
            'title',
            'description',
            'created_by',
            'created_at',
            'modified_at'
        ]


class RecipeViewSet(ModelViewSet):
    permission_class = []
    authentication_classes = []
    # permission_classes = [
    #     TokenPermission
    # ]
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_serializer_class(self):
        if self.action == 'list':
            return RecipeListSerializer
        return RecipeSerializer

    def get_queryset(self):
        queryset = recipe_models.Recipe.objects.all()

        queryset = queryset.select_related('created_by')

        if self.action == 'list':
            queryset = queryset.only(
                'id',
                'title',
                'description',
                'created_by__username',
                'created_at',
                'modified_at'
            )

        return queryset
