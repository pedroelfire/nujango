from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = "__all__"
        
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"

class MealToClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealToClient
        fields = "__all__"

class DailyMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMeal
        fields = "__all__"
