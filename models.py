from django.db import models
from msilib.schema import Class
from tkinter import CASCADE
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class producto(models.Model):
    id_producto = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=65)
    descripcion = models.TextField()
    precio = models.IntegerField()
    fec_publi = models.DateField()
    imagen = models.ImageField(upload_to="imgs_producto")

    def __str__(self):
        return self.nombre

class persona (models.Model):
    rut = models.CharField(primary_key=True,max_length=13)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    correo = models.CharField(max_length=60)
    direccion = models.CharField(max_length=75)
    nombre_usuario = models.CharField(max_length=50)
    vendedor = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.rut
        
class carrito (models.Model):
    id_carr = models.IntegerField(primary_key=True)
    persona = models.ForeignKey(persona,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return str(self.id_carr)

class pedidos (models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=75)
    cliente = models.ForeignKey(persona,on_delete=models.PROTECT)
    tar_cred = models.CharField(max_length=30)
    
    def __str__(self):
        return str(self.id_pedido)
    
class det_pedido (models.Model):
    id_det_pedido = models.IntegerField(primary_key=True)
    pedido = models.ForeignKey(pedidos,on_delete=models.CASCADE,max_length=10)
    cant_produ = models.IntegerField()
    total_prec = models.IntegerField()
    

    def __str__(self):
        return str(self.id_det_pedido)

class estado_pedido (models.Model):
    id_estado = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()

    def __str__(self):
        return str(self.id_estado)
    
class envio_pedido (models.Model):
    id_envio = models.IntegerField(primary_key=True)
    dir_envio = models.CharField(max_length=120)


    def __str__(self):
        return str(self.id_envio)


class prod_carrito (models.Model):
    id_prod_carrito = models.BigAutoField(primary_key=True)
    producto = models.ForeignKey(producto,on_delete=models.PROTECT)