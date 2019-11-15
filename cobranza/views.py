from django.shortcuts import render, redirect
from .models import CustomUser
from django.views.generic import CreateView
from django.views.generic import UpdateView
from .forms import *
from .models import *
from . import forms
from django.views import generic

# Create your views here.
def ruta_crear(request):
	if request.method == "POST":
		form = forms.CrearRuta(request.POST)
		if form.is_valid():
			form.save()
			return redirect("http://127.0.0.1:8000/Dashboard")
	form = forms.CrearRuta()
	return render(request, "cobranza/agregar_ruta.html", {'form': form})

def ruta_modificar(request, pk):
	user = Ruta()
	instance = Ruta.objects.get(pk=pk)
	if request.method == "POST":
		form = forms.ModificarRuta(request.POST, instance = instance)
		if form.is_valid():
			form.save()
			return redirect("http://127.0.0.1:8000/Dashboard")
	form = forms.ModificarRuta(instance = instance)
	return render(request, "cobranza/modificar_ruta.html", {'form': form})

class Rutas_List_View(generic.ListView):
	model = Ruta
