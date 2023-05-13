from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=128, verbose_name="Nombre")
    apellido = models.CharField(max_length=128, verbose_name="Apellido")
    mail = models.EmailField(max_length=128, verbose_name="Email")
    dni = models.IntegerField(verbose_name="Dni", null=True)


class DetalleAlumno(models.Model):
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento", default='1900-01-01')
    fecha_ingreso = models.DateField(verbose_name="Fecha de ingreso al sistema", default='1900-01-01')
    direccion = models.CharField(max_length=256, verbose_name="Dirección")
    mail_alternativo = models.EmailField(max_length=128, verbose_name="Email alternativo")
    titulo = models.BooleanField(verbose_name="Titulo secundario entregado")
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE, primary_key=True) # Uno a uno


class Instructor(models.Model):
    nombre = models.CharField(max_length=128, verbose_name="Nombre")
    apellido = models.CharField(max_length=128, verbose_name="Apellido")
    mail = models.EmailField(max_length=128, verbose_name="Email")
    dni = models.IntegerField(verbose_name="Dni", null=True)


class Curso(models.Model):
    comision = models.IntegerField(verbose_name="Número de comisión")
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE) # Muchos a uno
    alumnos = models.ManyToManyField(Alumno)
