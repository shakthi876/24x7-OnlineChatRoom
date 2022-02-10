from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
    def __str__(self):
        return self.name
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.CharField(max_length=15)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    time = models.CharField(max_length=16)

    def __str__(self):
        return self.user