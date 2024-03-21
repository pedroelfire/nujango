from django.db import models

# Create your models here.
UNIT_CHOICES = [
    ('g', 'grams'),
    ('ml', 'milliliters'),
    ('tbsp', 'tablespoons'),
]

class Ingredients(models.Model):
    food_id = models.JSONField(null=True)
    metric_serving_unit = models.CharField(choices=UNIT_CHOICES, max_length=4)
    metric_serving_amount = models.DecimalField(max_digits=10, decimal_places=3)


class Meal(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredients)
    
    def ola(self):
        print('ola')
    
    def __repr__(self):
        return (f"Nombre: {self.name}, Ingredientes: {self.ingredients}")
        



