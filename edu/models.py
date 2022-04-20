from django.db import models

# Create your models here.
class Destination1(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    phone = models.IntegerField(1000000000)
    Password = models.IntegerField(1000)
    address = models.CharField(max_length=100)