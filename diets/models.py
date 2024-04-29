from django.db import models
from client.models import Nutritionist, Client


# Create your models here.
UNIT_CHOICES = [
    ('g', 'grams'),
    ('ml', 'milliliters'),
    ('tbsp', 'tablespoons'),
]

class Ingredients(models.Model):
    food_id = models.IntegerField(null=True)
    metric_serving_unit = models.CharField(choices=UNIT_CHOICES, max_length=4)
    metric_serving_amount = models.DecimalField(max_digits=10, decimal_places=3)

    def __repr__(self):
        return (f"Nombre: {self.name}, Ingredientes: {self.ingredients}")

class Meal(models.Model):
    name = models.CharField(max_length=255)
    meal_time = models.TimeField(null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredients, default=0, blank=True)
    created_by = models.ForeignKey(Nutritionist, on_delete=models.DO_NOTHING)
 
    
class Diet(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(Nutritionist, on_delete=models.DO_NOTHING)
    meals = models.ManyToManyField(Meal, blank=True)
    
class MealToClient(models.Model):
    diet = models.OneToOneField(Diet, on_delete=models.DO_NOTHING)
    client = models.OneToOneField(Client, on_delete=models.DO_NOTHING)
    

