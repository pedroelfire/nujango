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

    def create(self, request, *args, **kwargs):
        print(request.data["username"])
        try:
            user = User.objects.create_user(username=request.data["username"], email=request.data["email"], password=request.data["password"])
            return JsonResponse({'message': 'Creacion de usuario exitosa'})

        except json.JSONDecodeError:
            return JsonResponse({'message': 'Error al decodificar JSON'}, status=400)

@csrf_exempt
def Auth(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = str(data.get('username'))
            password = str(data.get('password'))
            print(username, password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                return JsonResponse({'message': 'Autenticación exitosa'})
            else:
                return JsonResponse({'message': 'Autenticación fallida'}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Error al decodificar JSON'}, status=400)
    else:
        return JsonResponse({'message': 'Método no permitido'}, status=405)