from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from django.contrib.auth import authenticate, login, logout 
from fatsecret import Fatsecret
from django.db.models.signals import post_save
from django.views.decorators.csrf import csrf_exempt
import json

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

@csrf_exempt
def Auth(request):
    if request.method == 'POST':
        try:
            # Obtener los datos del cuerpo de la solicitud
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            print(username, password)
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                # Autenticación exitosa
                return JsonResponse({'message': 'Autenticación exitosa'})
            else:
                # Autenticación fallida
                return JsonResponse({'message': 'Autenticación fallida'}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Error al decodificar JSON'}, status=400)
    else:
        return JsonResponse({'message': 'Método no permitido'}, status=405)