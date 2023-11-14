from django.db import models

# Create your models here.

class Addition(models.model):
    nombre1 = models.IntegerField()
    nombre12 = models.IntegerField()
    resultat = models.IntegerField()