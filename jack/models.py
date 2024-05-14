from django.db import models
from client.models import *

# Create your models here.



class JackConversation(models.Model):
    made_by = models.ForeignKey(Client, on_delete=models.DO_NOTHING)

class JackQuestion(models.Model):
    question = models.CharField(max_length=400)
    response = models.CharField(max_length=10000)
    conversation = models.ForeignKey(JackConversation, on_delete=models.DO_NOTHING)

    
