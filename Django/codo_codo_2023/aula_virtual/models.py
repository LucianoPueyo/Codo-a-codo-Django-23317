from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=128, verbose_name="Nombre")
    apellido = models.CharField(max_length=128, verbose_name="Apellido")
    mail = models.EmailField(max_length=128, verbose_name="Email")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento", default='1900-01-01')
    dni = models.IntegerField(verbose_name="Dni", null=True)