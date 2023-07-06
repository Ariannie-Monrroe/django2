from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

import os
from .models import Categoria, Producto

from django.conf import settings
# Create your views here.

def cargarInicio(request):
    return render(request, "inicio.html")

@login_required
def cargarProductos(request):
    return render(request, "pProductos.html")

def exit(request):
    logout(request)
    return redirect('home')

def cargarAgregarProductos(request):
    return render (request, "agregarProductoBDD.html")

def agregarProducto(request):
    

    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])

    v_sku = request.POST['txtSku']
    v_nombre = request.POST['txtnombre']
    v_precio = request.POST['txtprecio']
    v_stock = request.POST['txtStock']
    v_descripcion = request.POST['txtDescripcion']
    v_imagen = request.FILES['txtImagen']

    Producto.objects.create(sku = v_sku, nombre = v_nombre, precio = v_precio,stock = v_stock, descripcion = v_descripcion, imagenUrl=v_imagen,categoriaId = v_categoria)
    
    return redirect('/agregarProducto')


def cargarEditarProducto(request,sku):
    prod = Producto.objects.get(sku = sku)
    categoria = Categoria.objects.all()
    return render(request,"editarProducto.html",{"prod":prod, "cate":categoria})


def editarProducto(request):
    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])

    v_sku = request.POST['txtSku']
    productBDD = Producto.objects.get(sku = v_sku)
    v_nombre = request.POST['txtnombre']
    v_precio = request.POST['txtprecio']
    v_stock = request.POST['txtStock']
    v_descripcion = request.POST['txtDescripcion']


    try:
        v_imagen = request.FILES['txtImagen']
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(productBDD.imagenUrl))
        os.remove(ruta_imagen)
    except:
        v_imagen = productBDD.imagenUrl

    productBDD.nombre = v_nombre
    productBDD.precio = v_precio
    productBDD.stock = v_stock
    productBDD.descripcion = v_descripcion
    productBDD.categoriaId = v_categoria
    productBDD.imagenUrl = v_imagen
    
    productBDD.save()

    return redirect('/agregarProducto')



def eliminarProducto(cod_producto):
    producto = Producto.objects.get(sku = cod_producto)
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(producto.imagenUrl))
    os.remove(ruta_imagen)
    producto.delete()
    return redirect('/agregarProducto')