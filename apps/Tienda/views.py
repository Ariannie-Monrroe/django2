from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

def cargarInicio(request):
    return render(request, "inicio.html")

@login_required
def cargarProductos(request):
    return render(request, "pProductos.html")

def exit(request):
    logout(request)
    return redirect('home')