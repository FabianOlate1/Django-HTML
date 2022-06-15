from datetime import datetime
from math import degrees
from django.shortcuts import render, get_object_or_404, redirect
from aplicacion.forms import frmPersona
from aplicacion.models import persona
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import Group,User


# Create your views here.
@login_required()
@permission_required('is_vendedores')
def paginavendedores(request):
    return render(request,"aplicacion/paginavendedores.html")

def cambiarpassword(request):
    form=PasswordChangeForm(request.POST or None)
    contexto={
        "form":form
    }
    
    if request.method=="POST":
        form=PasswordChangeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="home")
    
    return render(request,"registration/cambiarpassword.html",contexto)
    

def registro(request):
    form=UserCreationForm(request.POST or None)
    contexto={
        "form":form
    }
    
    if request.method=="POST":
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            credenciales=authenticate(username=form.cleaned_data["username"],password=form.cleaned_data["password1"])
            login(request,credenciales)
            return redirect(to="perfilusuario")
    
    return render(request,"registration/registro.html",contexto)

def home(request):
    mensaje="Hola esto son mis datos"
    fecha=datetime.now()
    
    contexto={
        "msg":mensaje,
        "f":fecha
    }
    
    return render(request,"aplicacion/home.html",contexto)

@login_required()
def listado(request):
    personas=persona.objects.all()
    total=persona.objects.count()
    contexto={
        "personas":personas,
        "total":total
    }
    return render(request,"aplicacion/listado.html",contexto)

@login_required()
def crear(request):
    formulario=frmPersona(request.POST or None)
    
    contexto={
        "frm":formulario
    }
    
    if request.method=="POST":
        formulario=frmPersona(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listado")
    
   
    
    return render(request,"aplicacion/crear.html",contexto)
@login_required()
@permission_required('aplicacion.change_persona',raise_exception=True)
def modificar(request,id):
    persona=get_object_or_404(persona,rut=id)
    
    frm=frmPersona(instance=persona)
    contexto={
        "frm":frm,
        "id":id
    }
    
    if request.method=="POST":
        frm=frmPersona(data=request.POST,instance=persona)
        if frm.is_valid():
            persona_mod=persona.objects.get(rut=persona.rut)
            datos=frm.cleaned_data
            persona_mod.nombre=datos.get("nombre")
            persona_mod.apellido=datos.get("apellido")
            persona_mod.correo=datos.get("correo")
            persona_mod.save()
            return redirect(to="listado")
            
        
        
    return render(request,"aplicacion/modificar.html",contexto)

@login_required()
def eliminar(request,id):
    persona_tokill=get_object_or_404(persona,rut=id)
    contexto={
        "persona":persona_tokill
    }
    
    if request.method=="POST":
        persona_tokill.delete()
        return redirect(to="listado")
    
    
    return render(request,"aplicacion/eliminar.html",contexto)

# Create your views here.
def home(request):
    return render(request, 'aplicacion/home.html')

def quienessomos(request):
    return render(request, 'aplicacion/quienessomos.html')    

def productos(request):
    return render(request, 'aplicacion/productos.html')

def api(request):
    return render(request, 'aplicacion/api.html')    

def carrito(request):
    return render(request, 'aplicacion/carrito.html') 

def perfil(request):
    return render(request, 'aplicacion/perfil.html') 

def login(request):
    return render(request, 'aplicacion/login.html') 