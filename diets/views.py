from django.shortcuts import render
from django.http import HttpResponse
from fatsecret import Fatsecret
from rest_framework.viewsets import ModelViewSet
from .serializers import *
import json
from .models import *
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


fs = Fatsecret("d7e8131ea6784224b25519d75aba04a6", "d2259ddb4d2f4fe9bb8c47c8ed1638b7")
foods = fs.food_get_v2("35755")
print(foods)

# Create your views here.


def hola(request):
    return HttpResponse(json.dumps(foods))

class IngredientsViewSet(ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer


class MealViewSet(ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    @receiver(post_save, sender=Meal)
    def my_handler(sender, **kwargs):
        obj = kwargs['instance']
        print('paso algo omaigad')
        

