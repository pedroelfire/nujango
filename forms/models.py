from django.db import models
from client.models import *
# Create your models here.

class Question(models.Model):
    nutritionist = models.OneToOneField(Nutritionist, on_delete=models.DO_NOTHING)
    question_text = models.CharField(max_length=400)

class Questionary(models.Model):
    questions = models.ManyToManyField(Question)

class QuestionaryToClient(models.Model):
    questionary = models.OneToOneField(Questionary, on_delete=models.DO_NOTHING)
    clients = models.ManyToManyField(Client, related_name="clients")