from django.db import models
from users.models import CustomUser


class Propietario(models.Model):
	rut = models.CharField(null=False, max_length=30)
	nombres = models.CharField(null=False, max_length=30)
	ap_paterno = models.CharField(null=False, max_length=30)
	ap_materno = models.CharField(null=False, max_length=30)
	direccion = models.CharField(null=False, max_length=30)
	nro = models.IntegerField(null=False)
	comuna = models.CharField(null=False, max_length=30)
	fono_residencial = models.IntegerField(null=False)
	direccion_correo_electronico = models.CharField(null=False, max_length=30)

class Estado_Visita(models.Model):
	id_estado_visita = models.IntegerField(null=False)
	nombres_estado_visita = models.IntegerField(null=False)


# Create your models here.
class Ruta(models.Model):
	id_ruta = models.IntegerField(null=False)
	cobrador = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	fecha_Ruta = models.DateTimeField()
	def MostrarRutas():
		return True;

# Create your models here.
class Visita(models.Model):
	id_visita = models.IntegerField(null=False)
	Observaciones = models.CharField(null=False, max_length=300)
	cliente = models.ForeignKey(Propietario, on_delete=models.CASCADE)
	estado_visita = models.ForeignKey(Estado_Visita, on_delete=models.CASCADE)
	ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
	def MostrarRutas():
		return True;