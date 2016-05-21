from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Compra(models.Model):
	proveedor = models.ForeignKey('proveedores.Proveedor', on_delete=models.CASCADE,)
	fecha = models.DateTimeField(auto_now_add=True, blank = True)
	nota = models.CharField(null=True, blank=True, max_length=100)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return str(self.proveedor.nombre + self.fecha.strftime('%d-%m-%Y %H:%M'))

	def __unicode__(self):
		return str(self.proveedor.nombre + self.fecha.strftime('%d-%m-%Y %H:%M'))

class Compra_detalle(models.Model):
	compra = models.ForeignKey('compras.Compra', on_delete = models.CASCADE)
	producto = models.ForeignKey('productos.Producto', on_delete = models.CASCADE)
	cantidad = models.IntegerField(default = 1)

	def __str__(self):
		return str(self.compra)

	def __unicode__(self):
		return str(self.compra + self.producto)
