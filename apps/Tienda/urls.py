
from django.urls import path 
from .views import cargarInicio, cargarProductos , exit, cargarAgregarProductos, cargarCrearUsuario, agregarProducto, crearUsuario,cargarEditarProducto,editarProducto,eliminarProducto

urlpatterns = [
    path('', cargarInicio, name= 'home'),
    path('pProductos.html/', cargarProductos , name='prod'),
    path('logout/', exit , name='exit'),
    path('agregarProductoBDD.html/', cargarAgregarProductos , name='cargar_P_BDD'),
    path('crearUsuario.html/', cargarCrearUsuario , name='crearUsuario'),
    
    path('agregarProductoF',agregarProducto),
    path('ValidarUsuario',crearUsuario),
    
    
    path('editarProducto/<sku>',cargarEditarProducto),
    
    path('editarProducto',editarProducto),
    
    path('eliminarProducto/<codigo>',eliminarProducto, name= 'eliminarProducto')
    

]
