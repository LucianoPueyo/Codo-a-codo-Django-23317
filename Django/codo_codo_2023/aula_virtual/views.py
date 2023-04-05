from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

def landing_page(request):
    print(reverse('alta_alumno'))
    print(request.method)

    return HttpResponse("<h1>Bienvenid@</h1> al Aula Virtual 2.0", status=208)

def saludar_usuario(request, nombre_usuario):
    return HttpResponse(f"Hola <b>{nombre_usuario}</b>, Bienvenid@ al Aula Virtual 2.0")

def alta_alumno(request):
    return HttpResponse("<h2>Alta de nuevos alumnos</h2>")

def baja_alumno(request):
    return HttpResponse("<h2>Baja de alumnos activos</h2>")

def listar_alumnos_2023(request):
    return HttpResponse(
        "<h2>Listado de alumnos 2023</h2>" + 
        "<p>1 - Carlos Lopez</p>" + 
        "<p>2 - Maria Del Cerro</p>" + 
        "<p>3 - Jorge Gomez</p>" 
    )

def listar_alumnos_by_year(request, year):
    if int(year) < 2020:
        return HttpResponseNotFound("<h2>No hay datos previos al año 2020</h2>")

    return HttpResponse(
        f"<h2>Listado de alumnos {year}</h2>" + 
        "<p>Josefina Perez (2023)</p>" + 
        "<p>Raul Diaz (2022)</p>" + 
        "<p>Micaela Gonzalez(2021)</p>" 
    )
    
def listar_alumnos_by_year_month(request, year, month):
    if int(year) < 2020:
        return HttpResponseNotFound("<h2>No hay datos previos al año 2020</h2>")

    if int(month) > 4:
        return HttpResponseNotFound("<h2>Sólamente hay datos para el primer cuatrimestre del año</h2>")
    
    return HttpResponse(
        f"<h2>Listado de alumnos año:{year} mes:{month}</h2>" + 
        f"<p>Josefina Perez ({month}/{year})</p>" + 
        f"<p>Raul Diaz ({month}/{year})</p>" + 
        f"<p>Micaela Gonzalez({month}/{year})</p>" 
    )

def docentes_by_year(request, year, curso):
    print(curso)
    return HttpResponse(
        f"<h2>Listado de docentes año: {year} del curso: {curso}</h2>" + 
        "<p>Docente 1</p>" + 
        "<p>Docente 2</p>"
    )