from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

def index(request):
    print(reverse('alta_alumno'))
    print(request.method)

    # Vamos a suponer que esta info la obtuve de la BBDD.
    alumno_ficticio = {
        'first_name': 'Pedro',
        'last_name': 'Del Cerro',
        'age': 35,
        'valid': False
    }

    # Este listado de alumnos tambien vamos a suponer que viene de la BBDD
    alumn_list = [
        {
            'first_name': 'Gonzalo',
            'last_name': 'Gutierrez',
            'age': 35,
            'valid': False
        },
        {
            'first_name': 'Maria',
            'last_name': 'Mocoretá',
            'age': 40,
            'valid': True
        },
        {
            'first_name': 'Gabriel',
            'last_name': 'Gonzalez',
            'age': 32,
            'valid': True
        },
    ]
    context = {
        'user_name': 'Carlos',
        'user_lastname': 'Lopez',
        'simulated_alumn': alumno_ficticio,
        'alumn_list': alumn_list
    }

    return render(request, 'aula_virtual/index.html', context)

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