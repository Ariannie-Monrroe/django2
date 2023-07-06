
from django.urls import path 
from .views import cargarInicio, cargarProductos , exit, cargarAgregarProductos, cargarCrearUsuario, agregarProducto, crearUsuario

urlpatterns = [
    path('', cargarInicio, name= 'home'),
    path('pProductos.html/', cargarProductos , name='prod'),
    path('logout/', exit , name='exit'),
    path('agregarProductoBDD.html/', cargarAgregarProductos , name='cargar_P_BDD'),
    path('crearUsuario.html/', cargarCrearUsuario , name='crearUsuario'),
    path('agregarProductoF',agregarProducto),
    path('ValidarUsuario',cargarCrearUsuario),
]
