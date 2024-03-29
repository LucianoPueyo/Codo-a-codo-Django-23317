from typing import Any, Dict
from django import forms
from django.core.exceptions import ValidationError
from .models import Alumno, Instructor

TYPE_CHOICES = [
    ("general", "General"),
    ("diploma_tramite", "Diploma en Tramite"),
    ("Constancia_alumno_regular", "Constancia de alumno regular"),
    ("otros", "Otros"),
]


class AltaAlumnoForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre", 
        widget=forms.TextInput(
            attrs={
                'id':'AltaAlumnoNombre',
                'class': 'campo_nombre rojo'
            }),
        required=True
    )
    apellido = forms.CharField(label="Apellido", required=True)
    mail = forms.EmailField(label="Email ", required=True)
    dni = forms.IntegerField(label="Dni", required=True)

    def clean(self):
        mail = self.cleaned_data["mail"]
        if Alumno.objects.filter(mail=mail).exists():
            raise ValidationError("Ya hay un alumno inscripto con ese mail")

        return self.cleaned_data

class AltaInstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'


class EnviarConsultaForm(forms.Form):
    mail = forms.EmailField(label="Email ", required=True)
    tipo = forms.ChoiceField(
        choices=TYPE_CHOICES,
    )

    fecha2 = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    mensaje = forms.CharField(widget=forms.Textarea(attrs={
                'class': 'area_texto'
            }))
