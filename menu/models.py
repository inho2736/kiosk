from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    image = models.ImageField()

class Menua(models.Model):
    name = models.CharField(max_length=200)
    