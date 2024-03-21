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

