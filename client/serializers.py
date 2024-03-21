from .models import *
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        
class NutritionistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutritionist
        fields = "__all__"
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"