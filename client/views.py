from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from django.contrib.auth import authenticate, login, logout 
from fatsecret import Fatsecret
from django.dispatch import receiver
from django.db.models.signals import post_save

fs = Fatsecret("d7e8131ea6784224b25519d75aba04a6", "d2259ddb4d2f4fe9bb8c47c8ed1638b7")

# Create your views here.

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer



class NutritionistViewSet(ModelViewSet):
    queryset = Nutritionist.objects.all()
    serializer_class = NutritionistSerializer
    
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            username = request.data["username"]
            print(username)
            password = request.data["password"]
            print(password)
            user = authenticate(username=username, password=password)
            print(user)
            return super().create(request, *args, **kwargs)
        except:
            return HttpResponse("Usuario culero mal")
    
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


    @receiver(post_save, sender=User)
    def my_handler(sender, **kwargs):
        obj = kwargs['instance']
        print('paso algo omaigad')

