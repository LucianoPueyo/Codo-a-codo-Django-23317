from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

from .forms import AltaAlumnoForm, EnviarConsultaForm
from .models import Alumno

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

    lista_alumnos = Alumno.objects.all()
    print(lista_alumnos.query)

    context = {
        'user_name': 'Carlos',
        'user_lastname': 'Lopez',
        'simulated_alumn': alumno_ficticio,
        'alumn_list': lista_alumnos
    }

    return render(request, 'aula_virtual/index.html', context)

def saludar_usuario(request, nombre_usuario):
    return HttpResponse(f"Hola <b>{nombre_usuario}</b>, Bienvenid@ al Aula Virtual 2.0")

def alta_alumno(request):
    if request.method == "POST":
        # POST
        alta_alumno_form = AltaAlumnoForm(request.POST)

        # Validaciones
        if alta_alumno_form.is_valid():
            print(
                alta_alumno_form.cleaned_data['apellido'],
                alta_alumno_form.cleaned_data['nombre'],
                alta_alumno_form.cleaned_data['mail']
            )

            messages.add_message(
                request, messages.SUCCESS,
                'Alumno dado de alta Correctamente',
                extra_tags="clase_1 clase_2"
            )
            
            return redirect("index")

        else:
            messages.add_message(request, messages.ERROR, 'Ocurrió un error')

    else:
        # GET
        alta_alumno_form = AltaAlumnoForm()

    context = {'form': alta_alumno_form}

    return render(request, 'aula_virtual/alta_alumno.html', context)

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

def enviar_consulta(request):

    form = EnviarConsultaForm()
    context = {'form': form}

    return render(request, 'aula_virtual/enviar_consulta.html', context)