from django.urls import path, include
from rest_framework import routers
from .views import *

router =  routers.DefaultRouter()
router.register(r'client', ClientViewSet)
router.register(r'nutritionist', NutritionistViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]