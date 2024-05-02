from django.db import models
from client.models import Nutritionist, Client
from fatsecret import Fatsecret
fs = Fatsecret("d7e8131ea6784224b25519d75aba04a6", "d2259ddb4d2f4fe9bb8c47c8ed1638b7")



# Create your models here.
UNIT_CHOICES = [
    ('g', 'grams'),
    ('ml', 'milliliters'),
    ('tbsp', 'tablespoons'),
]

class Ingredients(models.Model):
    food_id = models.IntegerField(null=True)
    data = models.JSONField(null= False, default=0)
    metric_serving_unit = models.CharField(choices=UNIT_CHOICES, max_length=4)
    metric_serving_amount = models.DecimalField(max_digits=10, decimal_places=3)
    created_by = models.ForeignKey(Nutritionist, on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        if not self.data:
            self.data = fs.food_get(self.food_id)  # Llamada a la función fs.food_get
        super().save(*args, **kwargs)


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
    

