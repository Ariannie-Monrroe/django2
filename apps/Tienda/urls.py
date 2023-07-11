
from django.urls import path 
from .views import agregar_carrito,cargarInicio,eliminar_stock, cargarProductos , exit, cargarAgregarProductos, cargarCrearUsuario, agregarProducto, crearUsuario,cargarEditarProducto,editarProducto,eliminarProducto

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
    
    path('eliminarProducto/<codigo>',eliminarProducto, name= 'eliminarProducto'),
    
    
    
    path('pProductos.html/<int:producto_id>/', eliminar_stock, name='eliminar_stock'),
    
    
    

    
    path('pProductos.html/<str:producto_id>/', agregar_carrito, name='agregar_carrito'),

]
