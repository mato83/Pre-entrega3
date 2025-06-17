from django import forms
from django.core.validators import RegexValidator

 
class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()



class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    dni = forms.CharField(max_length=8, validators=[RegexValidator(r'^\d{1,8}$', 'Solo se permiten números en este campo.')])
    NumeroLegajo = forms.CharField(max_length=5, validators=[RegexValidator(r'^\d{1,8}$', 'Solo se permiten números en este campo.')])
    email = forms.EmailField()
    

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    dni = forms.CharField(max_length=8, validators=[RegexValidator(r'^\d{1,8}$', 'Solo se permiten números en este campo.')])
    NumeroEmpleado = forms.CharField(max_length=30)
    email = forms.EmailField()
