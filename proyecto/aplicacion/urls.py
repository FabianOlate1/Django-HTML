from proyecto.urls import path, include
from aplicacion.views import cambiarpassword, carrito, home, micuenta, productoViewSet, quienessomos, productos, api, crear, eliminar, home, listado, modificar, paginavendedores, login, registro,agregar_producto,limpiar_carrito,eliminar_producto,restar_producto, perfilusuario
from rest_framework import routers

router = routers.DefaultRouter()
router.register("producto", productoViewSet)

# Patterns
urlpatterns = [
    path('', home,name="home"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('productos/', productos, name="productos"),
    # path('api/', api, name="api"),
    path('api/', include(router.urls)),
    path('micuenta/', micuenta, name="micuenta"),
    path('carrito/', carrito, name="carrito"),
    path('listado/',listado,name="listado"),
    path('crear/',crear,name="crear"),
    path('modificar/<id>',modificar,name="modificar"),
    path('eliminar/<id>',eliminar,name="eliminar"),
    path('paginavendedores/',paginavendedores,name='paginavendedores'),
    path('login/',login,name='login'),
    path('registro/',registro,name='registro'),
    path('cambiarpassword/',cambiarpassword,name='cambiarpassword'),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('perfilusuario/', perfilusuario,name='perfilusuario'),

]