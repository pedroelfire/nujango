from django.shortcuts import render
from .serializer import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class JackQuestionViewSet(ModelViewSet):
    queryset = JackQuestion.objects.all()
    serializer_class = JackQuestionSerializer
    
    def create(self, request, *args, **kwargs):
        food_id = request.data['food_id']
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        print('Hola (update)')
        print(request.data)
        return super().update(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        print('chupame los huevos(list)')
        print(request.data)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        print('ola(retrieve)')
        return super().retrieve(request, *args, **kwargs)