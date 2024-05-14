from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework.authtoken.views import ObtainAuthToken

router =  routers.DefaultRouter()
router.register(r'client', ClientViewSet)
router.register(r'nutritionist', NutritionistViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", LoginView.as_view()),
    path("restricted/", RestrictedView.as_view()),
    path("verify/:id/:accestoken", confirmVerificationEmail)
]