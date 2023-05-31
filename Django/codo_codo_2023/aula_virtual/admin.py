from django.contrib import admin

from .models import Alumno, DetalleAlumno, Instructor, Curso

admin.site.register(Alumno)
admin.site.register(DetalleAlumno)
admin.site.register(Instructor)
admin.site.register(Curso)