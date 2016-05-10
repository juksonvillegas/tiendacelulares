from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Proveedor(models.Model):
	ruc = models.CharField(max_length = 11, blank = False)
	nombre = models.CharField(max_length = 70, blank = False)
	direccion = models.CharField(max_length = 100)
	telefono = models.CharField(max_length = 9, blank = False)

	def __unicode__(self):
		return self.ruc

	def __str__(self):
		return self.nombre