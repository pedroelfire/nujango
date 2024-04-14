from django.db import models
from client.models import Nutritionist, Client


# Create your models here.
UNIT_CHOICES = [
    ('g', 'grams'),
    ('ml', 'milliliters'),
    ('tbsp', 'tablespoons'),
]

class Meal(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.OneToOneField(Nutritionist, on_delete=models.DO_NOTHING)
    meal_time = models.TimeField(null=True, blank=True)
    
class Ingredients(models.Model):
    food_id = models.IntegerField(null=True)
    metric_serving_unit = models.CharField(choices=UNIT_CHOICES, max_length=4)
    metric_serving_amount = models.DecimalField(max_digits=10, decimal_places=3)
    meal_id = models.ForeignKey(Meal, on_delete=models.DO_NOTHING, null=True, default=0)

    def __repr__(self):
        return (f"Nombre: {self.name}, Ingredientes: {self.ingredients}")
    
class DailyMeal(models.Model):
    name = models.CharField(max_length=255)
    meals = models.ManyToManyField(Meal, null=True)
    
class MealToClient(models.Model):
    meal = models.OneToOneField(DailyMeal, on_delete=models.DO_NOTHING)
    client = models.OneToOneField(Client, on_delete=models.DO_NOTHING)
    

