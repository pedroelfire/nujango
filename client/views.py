from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from django.contrib.auth import authenticate, login, logout 
from fatsecret import Fatsecret
from django.db.models.signals import post_save
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail

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
            user = User.objects.create_user(username=request.data["username"], email=request.data["email"], password=request.data["password"], is_active = False )
            refresh = RefreshToken.for_user(user)
            sendVerificationEmail(user, refresh)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Usuario creado exitosamente'
            })
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
    
def sendVerificationEmail(user, refresh):
    send_mail(
        "Subject here",
        f"Pulsa el siguiente link para confirmar tu correo electrónico: https://127.0.0.1:8000/verify/{user.id}/{refresh.access_token}",
        "from@example.com",
        [user.email],
        fail_silently=False,
    )
    
def confirmVerificationEmail(request):
    print(request.params)