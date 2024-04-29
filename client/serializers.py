from .models import *
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Client
        fields = "__all__"
        
class NutritionistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutritionist
        fields = "__all__"
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', "is_active"]
        #extra_kwargs = {'password': {'write_only': True, 'required': True}}

    """def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user"""
