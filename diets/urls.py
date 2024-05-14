from django.urls import path, include
from rest_framework import routers
from .views import *

router =  routers.DefaultRouter()
router.register(r'meals', MealViewSet)
router.register(r'ingredients', IngredientsViewSet)
router.register(r'mealtoclient', MealToClientViewSet)
router.register(r'diets', DietViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('createIngredientsMeal/', createIngredientsMeal),
    path('searchIngredients/', FSFunctions.as_view()),
    path('searchIngredients/<int:food_id>/', FSFunctions.as_view()),
    path('dietsNutritionist/', DietsNutritionist.as_view()),
    path('dietsNutritionist/<int:nutritionist_id>/', DietsNutritionist.as_view()),
    ]