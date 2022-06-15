from django.urls import path
from .views import cambiarpassword, carrito, home, perfil, quienessomos, productos, api, crear, eliminar, home, listado, modificar, paginavendedores, login, registro

urlpatterns = [
    path('', home,name="home"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('productos/', productos, name="productos"),
    path('api/', api, name="api"),
    path('perfil/', perfil, name="perfil"),
    path('carrito/', carrito, name="carrito"),
    path('listado/',listado,name="listado"),
    path('crear/',crear,name="crear"),
    path('modificar/<id>',modificar,name="modificar"),
    path('eliminar/<id>',eliminar,name="eliminar"),
    path('paginavendedores/',paginavendedores,name='paginavendedores'),
    path('login/',login,name='login'),
    path('registro/',registro,name='registro'),
    path('cambiarpassword/',cambiarpassword,name='cambiarpassword'),
]

