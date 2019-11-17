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
    path('AddUser', TemplateView.as_view(template_name='users/AddUser.html'), name='AddUser.html'), # new
    path(''
         'add/', views.usuario_crear, name='person_add'),
    path('<int:pk>/edit/', views.usuario_modificar, name='person_add'),
    path('listar/', views.Usuarios_List_View.as_view(), name='books'),
    path('gestionar_usuario/', views.gestionar_usuario, name='gesti_usuario'),  # new
]