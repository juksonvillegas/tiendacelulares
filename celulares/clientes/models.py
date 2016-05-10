from django.db import models

# Create your models here.
class Cliente(models.Model):
	dni = models.CharField(max_length = 8, blank = False)
	nombre = models.CharField(max_length = 70, blank = False)
	nacimiento = models.DateField(blank = False)
	sexo = models.BooleanField()
	direccion = models.CharField(max_length = 100, blank = False)
	email = models.EmailField(blank = False)
	telefono = models.CharField(max_length = 9, blank = False)
	mayorista = models.BooleanField(default=False)

	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return self.nombre