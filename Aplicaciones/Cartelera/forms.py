#CORREO ELECTRONICO
from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label='Nombre', required=True, max_length=20)
    email=forms.CharField(label='Email', required=True, max_length=30)
    contenido=forms.CharField(label='Contenido', required=True, max_length=400, widget=forms.Textarea)
