from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Consignacion(models.Model):
	cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE,)
	fecha = models.DateTimeField(auto_now_add=True, blank = True)
	nota = models.CharField(null=True, blank=True, max_length=100)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return str(self.cliente.nombre + " "+ self.fecha.strftime('%d-%m-%Y %H:%M'))

	def __unicode__(self):
		return str(self.cliente.nombre + " " + self.fecha.strftime('%d-%m-%Y %H:%M'))

class Consignacion_detalle(models.Model):
	consignacion = models.ForeignKey('ventas.Consignacion', on_delete = models.CASCADE)
	producto = models.ForeignKey('productos.Producto', on_delete = models.CASCADE)
	cantidad = models.IntegerField(default = 1)

	def __str__(self):
		return str(self.consignacion + self.producto)

	def __unicode__(self):
		return str(self.consignacion + self.producto)

class Venta(models.Model):
	cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE,)
	fecha = models.DateTimeField(auto_now_add=True, blank = True)
	documentado = models.BooleanField(default = False)
	estado = models.BooleanField(default = True)

	def __str__(self):
		return str(self.fecha.strftime('%d-%m-%Y %H:%M'))

	def __unicode__(self):
		return str(self.fecha.strftime('%d-%m-%Y %H:%M'))

class Venta_detalle(models.Model):
	venta = models.ForeignKey('ventas.Venta', on_delete = models.CASCADE)
	producto = models.ForeignKey('productos.Producto', on_delete = models.CASCADE)
	cantidad = models.IntegerField(default=1)
	precio = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return str(self.producto.nombre)

	def __unicode__(self):
		return str(self.producto.nombre)
