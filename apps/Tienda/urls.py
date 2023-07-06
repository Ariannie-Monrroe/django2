
from django.urls import path 
from .views import cargarInicio, cargarProductos , exit

urlpatterns = [
    path('', cargarInicio, name= 'home'),
    path('pProductos.html/', cargarProductos , name='prod'),
    path('logout/', exit , name='exit'),

]
