"""ElLugarFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include # new
from django.views.generic.base import TemplateView # new
from . import views

urlpatterns = [
    path('add/', views.ruta_crear, name='ruta_add'),
    path('<int:pk>/edit/', views.ruta_modificar, name='ruta_edit'),
    path('listar/', views.Rutas_List_View.as_view(), name='ruta_list'),
    path('vista/add/', views.ruta_crear, name='vista_add'),
    path('vista/<int:pk>/edit/', views.visita_modificar, name='vista_edit'),
    path('vista/listar/', views.Visitas_List_View.as_view(), name='vista_list'),
]