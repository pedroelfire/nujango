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
    path('searchListIngredients/', searchListIngredients),
    path('searchIngredient/<int:food_id>/', searchIngredient),
    path('getDietsByNutritionistId/<int:nutritionist_id>/', getDietsByNutritionistId),
    ]