import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from fatsecret import Fatsecret
from rest_framework.viewsets import ModelViewSet
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
from rest_framework.decorators import action



fs = Fatsecret("d7e8131ea6784224b25519d75aba04a6", "d2259ddb4d2f4fe9bb8c47c8ed1638b7")
foods = fs.food_get_v2(food_id="35755")

# Create your views here.

class IngredientsViewSet(ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer

    def create(self, request, *args, **kwargs):
        food_id = request.data['food_id']
        fs.food_get(food_id)
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):

        return super().update(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
   
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):

        return super().retrieve(request, *args, **kwargs)

class MealViewSet(ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class MealToClientViewSet(ModelViewSet):
    queryset = MealToClient.objects.all()
    serializer_class = MealToClientSerializer
    
class DietViewSet(ModelViewSet):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer

class DietsNutritionist(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, nutritionist_id, format=None):
        diets = Diet.objects.filter(created_by=nutritionist_id)
        serializer = DietSerializer(diets, many=True)
        return Response({'message': 'Search Diets Succesfull', 'data': serializer.data})
    
    def post(self, request):
        return Response({'message': 'Search Diets Succesfull'})

class FSFunctions(APIView):
    def post(self, request):
        query = request.data['query_search']
        try:
            ingredients = fs.foods_search(query)
            return JsonResponse({'message': 'Search Succesfull', 'data': ingredients})
        except Exception as e:
            return JsonResponse({'message': "An error ocurred", "data":e}, status=400)
        
    def get(self, request, food_id):
        try:
            ingredient = fs.food_get_v2(food_id)
            return JsonResponse({'message': 'Search Succesfull', 'data': ingredient})
        except Exception as e:
            return JsonResponse({'message': "An error ocurred", "data": str(e)}, status=400)


@csrf_exempt
@api_view(['POST'])    
def addIngredientDiary(request):
    i = request
    client= Client.objects.get(id=request.data["created_by"])
    ingredient = Ingredients.objects.create(food_id=i['food_id'], metric_serving_unit=i['metric_serving_unit'], metric_serving_amount=i['metric_serving_amount'], created_by=client)
    return Response({'message': 'Ingredient added succesfully', 'data': ingredient})


@csrf_exempt
@api_view(['POST'])
def createIngredientsMeal(request):
    try:        
        ingredients_list = request.data['ingredients']
        client = Nutritionist.objects.get(id=request.data["created_by"])    
        meal = Meal.objects.create(name=request.data['name'], meal_time=request.data["meal_time"], created_by=client)
        for i in ingredients_list:
            fs.food_get_v2(i['food_id'])
            ingredient = Ingredients.objects.create(food_id=i['food_id'], data=i['data'], metric_serving_unit=i['metric_serving_unit'], metric_serving_amount=i['metric_serving_amount'], created_by=client)
            meal.ingredients.add(ingredient)
        
        serializer = MealSerializer(meal)    
        return Response({'message': 'Meal created successfully', "data":serializer.data}, status=status.HTTP_201_CREATED)
    except Exception as e: return Response({'message': 'One of the ingredients does not exist', 'error': e})