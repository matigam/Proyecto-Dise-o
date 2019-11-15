from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    pass
    rut_usuario = models.CharField(max_length=30, null=False)
    nombres = models.CharField(max_length=30, null=False)
    apellidos = models.CharField(max_length=30, null=False)
    direccion = models.CharField(max_length=30, null=False)
    telefono_movil = models.IntegerField(null=False)
    telefono_residencial = models.IntegerField(null=False)
    correo = models.EmailField(null=False)


    def __str__(self):
        return self.username

class Supervisor(CustomUser):
	id_supervisor = models.IntegerField(null=False)

	def asignar_Ruta(Cobrador):
   		return True;
	def eliminar_visita():
		return True;
	def modificar_visita():
   		return True;
	def agregar_visita():
		return True;
	def asignar_perfil():
		return True;
	def asignar_usuario():
		return True;
	def modificar_usuario(self, formulario):
		formulario.save()
	def eliminar_usuario():
		return True;
	# Falta en el diagrama
	def agregar_usuario(self, formulario):
		formulario.save()

class Cobrador(CustomUser):
	id_cobrador = models.IntegerField(null=False)
	def MostrarRutas():
		return True;