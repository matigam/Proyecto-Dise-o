from django.db import models



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


# Create your models here.
class Visita(models.Model):
	id_visita = models.IntegerField(null=False)
	Observaciones = models.CharField(null=False, max_length=300)
	cliente = models.ForeignKey(Propietario, on_delete=models.CASCADE)
	def MostrarRutas():
		return True;

class Estado_Visita(models.Model):
	id_estado_visita = models.IntegerField(null=False)
	nombres_estado_visita = models.IntegerField(null=False)