from django.shortcuts import render
from django.http import HttpResponse

def landing_page(request):
    return HttpResponse("<h1>Bienvenid@</h1> al Aula Virtual 2.0")

def saludar_usuario(request, nombre_usuario):
    return HttpResponse(f"Hola <b>{nombre_usuario}</b>, Bienvenid@ al Aula Virtual 2.0")

def alta_alumno(request):
    return HttpResponse("<h2>Alta de nuevos alumnos</h2>")

def baja_alumno(request):
    return HttpResponse("<h2>Baja de alumnos activos</h2>")
