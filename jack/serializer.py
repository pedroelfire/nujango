from .models import *
from rest_framework import serializers

class JackConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JackConversation
        fields = "__all__"
        
class JackQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JackQuestion
        fields = "__all__"
