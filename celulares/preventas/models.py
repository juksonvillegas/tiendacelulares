from django.utils import timezone
from django.db import models
from datetime import datetime

# Create your models here.
class Preventa(models.Model):
	cliente = models.ForeignKey('clientes.Cliente', on_delete = models.CASCADE,)
	cantidad = models.IntegerField(default = 1)
	producto = models.ForeignKey('productos.Producto', on_delete = models.CASCADE,)
	fecha = models.DateTimeField(auto_now_add=True, blank = True)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return str(self.fecha.strftime('%d-%m-%Y %H:%M'))

	def __unicode__(self):
		return str(self.fecha.strftime('%d-%m-%Y %H:%M'))