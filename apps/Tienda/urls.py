
from django.urls import path 
from .views import cargarInicio, cargarProductos , exit, cargarAgregarProductos

urlpatterns = [
    path('', cargarInicio, name= 'home'),
    path('pProductos.html/', cargarProductos , name='prod'),
    path('logout/', exit , name='exit'),
    path('agregarProductoBDD.html/', cargarAgregarProductos , name='cargar_P_BDD'),

]
