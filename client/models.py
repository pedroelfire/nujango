from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    weight = models.DecimalField(decimal_places=3, max_digits=8)
    height = models.DecimalField(decimal_places=3, max_digits=8)
    
class Nutritionist(models.Model):
    user = models.OneToOneField(Client, on_delete=models.CASCADE)
    ced = models.CharField(max_length=255)
