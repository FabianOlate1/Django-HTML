from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import Group,User
from datetime import datetime
from math import degrees
from aplicacion.admin import admproducto
from aplicacion.forms import frmpersona
from aplicacion.models import pedidos, persona, producto
from aplicacion.Carrito import Carrito
from aplicacion.serializers import PedidoSrlz, ProductoSrlz
from rest_framework import viewsets

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
        form=PasswordChangeForm(
            
            data=request.POST)
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
    personas = persona.objects.all()
    total= persona.objects.count()
    contexto={
        "personas":personas,
        "total":total
    }
    return render(request,"aplicacion/listado.html",contexto)

@login_required()
def crear(request):
    formulario=frmpersona(request.POST or None)
    
    contexto={
        "frm":formulario
    }
    
    if request.method=="POST":
        formulario=frmpersona(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listado")
    
    return render(request,"aplicacion/crear.html",contexto)

@login_required()
@permission_required('aplicacion.change_persona',raise_exception=True)
def modificar(request,id):
    Persona=get_object_or_404(persona,rut=id)

    frm=frmpersona(request.POST, instance=Persona)
    contexto={
        "frm":frm,
        "id":id
    }
    
    if request.method=="POST":
        frm=frmpersona(data=request.POST,instance=Persona)
        if frm.is_valid():
            persona_mod=persona.objects.get(rut=Persona.rut)
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
    productos = producto.objects.all()
    contexto = {
        "productos": productos
    }
    return render(request, 'aplicacion/productos.html', contexto)

def api(request):
    return render(request, 'aplicacion/api.html')    

def micuenta(request):
    return render(request, 'aplicacion/micuenta.html') 

def login(request):
    return render(request, 'aplicacion/login.html') 

def perfilusuario(request):
    return render(request, 'aplicacion/perfilusuario.html') 


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    Producto = producto.objects.get(id_producto=producto_id)
    carrito.agregar(Producto)
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    Producto = producto.objects.get(id_producto=producto_id)
    carrito.restar(Producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")

def carrito(request):
    return render(request, 'aplicacion/carrito.html') 

class productoViewSet(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = ProductoSrlz
    
class pedidosViewSet(viewsets.ModelViewSet):
    queryset = pedidos.objects.all()
    serializer_class = PedidoSrlz