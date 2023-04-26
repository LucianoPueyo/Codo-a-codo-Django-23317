from django import forms
from django.core.exceptions import ValidationError

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

    def clean_nombre(self):
        pass
        # Validación del campo Nombre

        # Para mas detalle
        # https://docs.djangoproject.com/en/4.2/ref/forms/validation/

        # raise ValidationError("Validacion de nombre invalida")


class EnviarConsultaForm(forms.Form):
    mail = forms.EmailField(label="Email ", required=True)
    tipo = forms.ChoiceField(
        choices=TYPE_CHOICES,
    )

    fecha2 = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    mensaje = forms.CharField(widget=forms.Textarea(attrs={
                'class': 'area_texto'
            }))
