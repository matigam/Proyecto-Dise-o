from django.shortcuts import render, redirect
from .models import CustomUser
from django.views.generic import CreateView
from django.views.generic import UpdateView
from users.forms import *
from users.models import *
from . import forms
from django.views import generic




def usuario_crear(request):
	if request.method == "POST":
		form = forms.CrearUsuario(request.POST)
		if form.is_valid():
			usuario = Supervisor()
			usuario.agregar_usuario(form)
			return redirect("http://127.0.0.1:8000/Dashboard")
	form = forms.CrearUsuario()
	return render(request, "users/agregar_usuario.html", {'form': form})

def usuario_modificar(request, pk):
	user = CustomUser()
	instance = CustomUser.objects.get(pk=pk)
	if request.method == "POST":
		form = forms.ModificarUsuario(request.POST, instance = instance)
		if form.is_valid():
			usuario = Supervisor()
			usuario.modificar_usuario(form)
			return redirect("http://127.0.0.1:8000/Dashboard")
	form = forms.ModificarUsuario(instance = instance)
	return render(request, "users/modificar_usuario.html", {'form': form})

def gestionar_usuario(request):
	user = CustomUser()
	return render(request, 'users/gestionar_usuario.html', {})

class Usuarios_List_View(generic.ListView):
	model = CustomUser
