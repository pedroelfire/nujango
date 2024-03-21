from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from fatsecret import Fatsecret
from django.dispatch import receiver
from django.db.models.signals import post_save

fs = Fatsecret("d7e8131ea6784224b25519d75aba04a6", "d2259ddb4d2f4fe9bb8c47c8ed1638b7")

# Create your views here.

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    @receiver(post_save, sender=User)
    def my_handler(sender, **kwargs):
        obj = kwargs['instance']
        print('paso algo omaigad')


class NutritionistViewSet(ModelViewSet):
    queryset = Nutritionist.objects.all()
    serializer_class = NutritionistSerializer
    
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
