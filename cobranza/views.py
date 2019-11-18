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

# Create your views here.
def visita_crear(request):
	if request.method == "POST":
		form = forms.CrearVisita(request.POST)
		if form.is_valid():
			form.save()
			return redirect("http://127.0.0.1:8000/Dashboard")
	form = forms.CrearVisita()
	return render(request, "cobranza/agregar_visita.html", {'form': form})

def visita_modificar(request, pk):
	user = Ruta()
	instance = Visita.objects.get(pk=pk)
	if request.method == "POST":
		form = forms.ModificarVisita(request.POST, instance = instance)
		if form.is_valid():
			form.save()
			return redirect("http://127.0.0.1:8000/Dashboard")
	form = forms.ModificarVisita(instance = instance)
	return render(request, "cobranza/modificar_visita.html", {'form': form})

def editar_ruta(request):
	ruta = Ruta.objects.all()
	context = {'rutas': ruta}
	return render(request, 'cobranza/editar_ruta.html', context)

def editar_visita(request):
	visita = Visita.objects.all()
	context = {'visitas': visita}
	return render(request, 'cobranza/editar_visita.html', context)

class Visitas_List_View(generic.ListView):
	model = Visita

# Create your views here.
def propietario_crear(request):
	if request.method == "POST":
		form = forms.CrearPropietario(request.POST)
		if form.is_valid():
			form.save()
			return redirect("http://127.0.0.1:8000/Dashboard")
	form = forms.CrearPropietario()
	return render(request, "cobranza/agregar_propietario.html", {'form': form})

def propietario_modificar(request, pk):
	user = Ruta()
	instance = Propietario.objects.get(pk=pk)
	if request.method == "POST":
		form = forms.ModificarPropietario(request.POST, instance = instance)
		if form.is_valid():
			form.save()
			return redirect("http://127.0.0.1:8000/Dashboard")
	form = forms.ModificarPropietario(instance = instance)
	return render(request, "cobranza/modificar_propietario.html", {'form': form})

class Propietarios_List_View(generic.ListView):
	model = Propietario

# Create your views here.
def estado_visita_crear(request):
	if request.method == "POST":
		form = forms.CrearEstado_Visita(request.POST)
		if form.is_valid():
			form.save()
			return redirect("http://127.0.0.1:8000/Dashboard")
	form = forms.CrearEstado_Visita()
	return render(request, "cobranza/agregar_estado_visita.html", {'form': form})

def estado_visita_modificar(request, pk):
	user = Ruta()
	instance = Estado_Visita.objects.get(pk=pk)
	if request.method == "POST":
		form = forms.ModificarEstado_Visita(request.POST, instance = instance)
		if form.is_valid():
			form.save()
			return redirect("http://127.0.0.1:8000/Dashboard")
	form = forms.ModificarEstado_Visita(instance = instance)
	return render(request, "cobranza/modificar_estado_visita.html", {'form': form})
def gestionar_visitas(request):
	user = CustomUser()
	return render(request, 'cobranza/gestionar_visitas.html', {})
def modificar(request):
	user = CustomUser()
	return render(request, 'cobranza/modificar.html', {})

def editar_propietario(request):
	propietario = Propietario.objects.all()
	context = {'propietarios': propietario}
	return render(request, 'cobranza/editar_propietario.html', context)

class Estados_visita_List_View(generic.ListView):
	model = Estado_Visita
def editar_estado_visita(request):
	name = Estado_Visita.objects.all()
	context = {'names': name}
	return render(request, 'cobranza/editar_estado_visita.html', context)
