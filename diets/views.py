from django.shortcuts import render, redirect
from django.http import HttpResponse
from fatsecret import Fatsecret
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import *
import json
from .models import *
from rest_framework.decorators import action



fs = Fatsecret("d7e8131ea6784224b25519d75aba04a6", "d2259ddb4d2f4fe9bb8c47c8ed1638b7")
foods = fs.food_get_v2(food_id="35755")

# Create your views here.


def hola(request):
    return HttpResponse(json.dumps(foods))

class IngredientsViewSet(ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer


    def create(self, request, *args, **kwargs):
        food_id = request.data['food_id']
        fs.food_get(food_id)
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

class MealViewSet(ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    def retrieve(self, request, *args, **kwargs):
        nutritionist = request.created_by
        queryset = Meal.objects.filter(created_by=nutritionist)
        print(queryset)
        serializer = MealSerializer(queryset, many=True)
        return Response(serializer.data)

class MealToClientViewSet(ModelViewSet):
    queryset = MealToClient.objects.all()
    serializer_class = MealToClientSerializer
    
class DietViewSet(ModelViewSet):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer
    
def search_food(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        foods = fs.foods_search(query)
        print(foods)
        return render(request, 'search_results.html', {'foods': foods})
    return render(request, 'search_food.html')

