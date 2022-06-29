from django.contrib import admin

from aplicacion.models import carrito, det_pedido, estado_pedido, pedidos, persona, producto, envio_pedido


class admpersona(admin.ModelAdmin):
    list_display=["rut", "nombre", "apellido", "correo", "direccion", "nombre_usuario", "vendedor"]
    list_editable=["nombre", "apellido", "correo", "nombre_usuario", "vendedor"]
    
    class Meta:
        model= persona

admin.site.register(persona , admpersona)


class admproducto (admin.ModelAdmin):
    list_display=["id_producto", "nombre", "descripcion", "precio", "fec_publi", "imagen"]
    list_editable=["nombre", "descripcion", "precio"]

    class Meta:
        model= producto

admin.site.register(producto, admproducto)


class admcarrito(admin.ModelAdmin):
    list_display=["id_carr", "persona"]
    list_editable=["persona"]

    class Meta:
        model= carrito

admin.site.register(carrito, admcarrito)


class admpedidos(admin.ModelAdmin):
    list_display=["id_pedido", "direccion", "cliente"]
    list_editable=["direccion", "cliente"]

    class Meta:
        model= pedidos

admin.site.register(pedidos, admpedidos)


class admdet_pedido (admin.ModelAdmin):
    list_display=["id_det_pedido", "pedido", "cant_produ", "total_prec"]
    list_editable=["cant_produ"]

    class Meta:
        model= det_pedido

admin.site.register(det_pedido, admdet_pedido)


class admestado_pedido (admin.ModelAdmin):
    list_display=["id_estado", "nombre", "descripcion"]
    list_editable=["nombre", "descripcion"]

    class Meta:
        model= estado_pedido

admin.site.register(estado_pedido, admestado_pedido)

class admenvio_pedido(admin.ModelAdmin):
    list_display=["id_envio", "dir_envio"]
    list_editable=["dir_envio"]

    class Meta:
        model= envio_pedido

admin.site.register(envio_pedido, admenvio_pedido)



