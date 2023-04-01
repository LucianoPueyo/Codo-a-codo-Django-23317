from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('saludar/<str:nombre_usuario>', views.saludar_usuario, name='saludar_usuario'),
    path('alta_alumno', views.alta_alumno, name='alta_alumno'),
    path('baja_alumno', views.baja_alumno, name='baja_alumno')
]