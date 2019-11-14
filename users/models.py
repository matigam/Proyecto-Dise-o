from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    pass
    rut_usuario = models.CharField(max_length=30, null=False)

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
	def modificar_usuario():
		return True;
	def eliminar_usuario():
		return True;
	# Falta en el diagrama
	def agregar_usuario(User, Email, Password, Tipo_Usu):
		user = User.objects.create_user(User, Email, Password)
		user.save()

class Cobrador(CustomUser):
	id_cobrador = models.IntegerField(null=False)
	def MostrarRutas():
		return True;