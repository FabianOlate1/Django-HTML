from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from aplicacion.models import persona

class frmpersona(forms.ModelForm):
    
    class Meta:
        model=persona
        fields=["rut","nombre","apellido","correo","direccion","nombre_usuario"]


        