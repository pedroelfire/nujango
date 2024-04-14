from django.urls import path, include
from rest_framework import routers
from .views import *

router =  routers.DefaultRouter()
router.register(r'meals', MealViewSet)
router.register(r'ingredients', IngredientsViewSet)
router.register(r'mealtoclient', MealToClientViewSet)
router.register(r'dailymeal', DailyMealViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('search/', search_food, name='search_food'),
]