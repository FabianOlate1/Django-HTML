from aplicacion.admin import admproducto
from aplicacion.models import producto

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        id_producto = str(producto.id_producto)
        if id_producto not in self.carrito.keys():
            self.carrito[id_producto]={
                "producto_id": producto.id_producto,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id_producto]["cantidad"] += 1
            self.carrito[id_producto]["acumulado"] += producto.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id_producto = str(producto.id_producto)
        if id_producto in self.carrito:
            del self.carrito[id_producto]
            self.guardar_carrito()

    def restar(self, producto):
        id_producto = str(producto.id_producto)
        if id_producto in self.carrito.keys():
            self.carrito[id_producto]["cantidad"] -= 1
            self.carrito[id_producto]["acumulado"] -= producto.precio
            if self.carrito[id_producto]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True