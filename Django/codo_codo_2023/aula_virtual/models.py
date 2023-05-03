from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    mail = models.EmailField(max_length=128)