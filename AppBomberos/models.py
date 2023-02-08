from django.db import models

# Create your models here.

class Bombero(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    cargo = models.CharField(max_length=40)
    numero = models.CharField(max_length=30)
    division = models.CharField(max_length=40)

class division(models.Model):
    nombre_division = models.CharField(max_length=30)
    encargados_division = models.CharField(max_length=40)


class guardia(models.Model):
    
    dia = models.CharField(max_length=40)
    encargado_guardia = models.CharField(max_length=40)