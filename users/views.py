from django.shortcuts import render
from .models import CustomUser
from django.views.generic import CreateView
from django.views.generic import UpdateView
from users.forms import *
class UserCreateView(CreateView):
    model = CustomUser
    fields = ('rut_usuario', 'password', 'nombres', 'apellidos' , 'direccion' , 'telefono_movil', 'telefono_residencial', 'correo')





class UserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'users/customuser_update_form.html'