from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



from aplicacion.models import persona

class frmPersona(forms.ModelForm):
    
    class Meta:
        model=persona
        fields=["rut","nombre","apellido","correo"]
        
        
class frmCrearUsuario(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2"]  