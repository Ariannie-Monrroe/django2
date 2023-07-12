from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from time import sleep
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


import os

from .models import Categoria, Producto, Usuario

from django.conf import settings
# DEF Cargar TEMPLATES (INICIO)

@login_required
def cargarAgregarProductos(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request,"agregarProductoBDD.html",{"cate":categorias,"prod":productos})


def cargarEditarProducto(request,sku):
    productoEdit = Producto.objects.get(sku = sku)
    categoria = Categoria.objects.all()
    return render(request,"editProducto.html",{"prod":productoEdit, "cate":categoria })

def cargarInicio(request):
    
    return render(request, "inicio.html")


@login_required
def cargarProductos(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()

    return render(request, "pProductos.html",{"prod":productos, "cate":categorias})



def cargarCrearUsuario(request):
    crearUsuario
    
    return render(request, "crearUsuario.html")
# Cargar TEMPLATES (FIN)

# Crear usuario 
def crearUsuario(request):
    
    v_correo = request.POST['emailNuevo']
    v_nombreUsuario = request.POST['usernameNuevo']
    v_contrasena = request.POST['passwordNuevo']
    
    Usuario.objects.create(correo = v_correo, nombreUsuario = v_nombreUsuario, passUsuario = v_contrasena)
    
    messages.success(request, f'Usuario {v_nombreUsuario} creado correctamente')
    sleep(2)
    return redirect('home')


def exit(request):
    logout(request)
    return redirect('home')


# Editar, Eliminar, Agregar Producto como ADMINISTRADOR (INICIO)

def agregarProducto(request):
    
    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])
    v_sku = request.POST['txtSku']
    v_nombre = request.POST['txtnombre']
    v_precio = request.POST['txtprecio']
    v_stock = request.POST['txtStock']
    v_descripcion = request.POST['txtDescripcion']
    v_imagen = request.FILES['txtImagen']

    Producto.objects.create(sku = v_sku, nombre = v_nombre, precio = v_precio,stock = v_stock, descripcion = v_descripcion, imagenUrl=v_imagen,categoriaId = v_categoria)
    
    return redirect('/agregarProductoBDD.html')


def editarProducto(request):
    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])
    v_sku = request.POST['txtSku']
    productEditar = Producto.objects.get(sku = v_sku)
    v_nombre = request.POST['txtnombre']
    v_precio = request.POST['txtprecio']
    v_stock = request.POST['txtStock']
    v_descripcion = request.POST['txtDescripcion']

    try:
        v_imagen = request.FILES['txtImagen']
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(productEditar.imagenUrl))
        os.remove(ruta_imagen)
    except:
        v_imagen = productEditar.imagenUrl

    productEditar.nombre = v_nombre
    productEditar.precio = v_precio
    productEditar.stock = v_stock
    productEditar.descripcion = v_descripcion
    productEditar.categoriaId = v_categoria
    productEditar.imagenUrl = v_imagen
    
    productEditar.save()

    return redirect('/agregarProductoBDD.html')



def eliminarProducto(request,codigo):
    
    productoEliminar = Producto.objects.get(sku=codigo)
    eliminarImagen = os.path.join(settings.MEDIA_ROOT, str(productoEliminar.imagenUrl))
    os.remove(eliminarImagen)
    productoEliminar.delete()
    
    return redirect('/agregarProductoBDD.html')




    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad', 0))

        try:
            util_descontar_stock(producto_id, cantidad)
            return JsonResponse({'success': True})
        except ValueError as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})
# Agregar, Eliminar y Editar productos como ADMINISTRADOR (FIN)


#DESCONTAR STOCK
def eliminar_stock(request, producto_id):
    try:
        producto = Producto.objects.get(sku=producto_id)
        if producto.stock > 0:
            producto.stock -= 1
            producto.save()
            mensaje = "Compra realizada!!."
        else:
            mensaje = "No hay suficiente stock disponible."
    except Producto.DoesNotExist:
        mensaje = "Producto no encontrado."

    return render(request, 'pProductos.html', {'mensaje': mensaje})




