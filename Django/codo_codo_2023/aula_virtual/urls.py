from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('saludar/<str:nombre_usuario>/', views.saludar_usuario, name='saludar_usuario'),
    path('alta_alumno/', views.alta_alumno, name='alta_alumno'),
    path('alta_instructor/', views.alta_instructor, name='alta_instructor'),
    path('baja_alumno/', views.baja_alumno, name='baja_alumno'),

    path('listar_alumnos/', views.listar_alumnos, name='listar_alumnos'),
    path('listar_instructores/', views.ListarInstructores.as_view(), name='listar_instructores'),


    path('alumnos/2023/', views.listar_alumnos_2023, name="listar_alumnos_2023"),
    re_path(r'^alumnos/(?P<year>[0-9]{4})/$', views.listar_alumnos_by_year, name="listar_alumnos_by_year"),
    re_path(r'^alumnos/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.listar_alumnos_by_year_month, name="listar_alumnos_by_year_month"),

    path('docentes/<int:year>/', views.docentes_by_year, {'curso': 'Django'}, name="docentes_by_year"),

    path('enviar_consulta/', views.enviar_consulta, name="enviar_consulta"),
]