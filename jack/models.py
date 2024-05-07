from django.db import models
from client.models import *

# Create your models here.


class JackQuestion(models.Model):
    question = models.CharField(max_length=400)
    response = models.CharField(max_length=10000)

class JackConversation(models.Model):
    jack_question = models.ManyToManyField(JackQuestion, blank=True, on_delete=models.DO_NOTHING)
    made_by = models.ForeignKey(Client)
