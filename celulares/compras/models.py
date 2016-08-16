from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from productos.models import Almacen

# Create your models here.
class Compra(models.Model):
	proveedor = models.ForeignKey('proveedores.Proveedor', on_delete=models.CASCADE,)
	fecha = models.DateTimeField(auto_now_add=True, blank = True)
	documentado = models.BooleanField(default = False)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return str(self.proveedor.nombre + self.fecha.strftime('%d-%m-%Y %H:%M'))

	def __unicode__(self):
		return str(self.proveedor.nombre + self.fecha.strftime('%d-%m-%Y %H:%M'))

class Compra_detalle(models.Model):
	compra = models.ForeignKey('compras.Compra', on_delete = models.CASCADE)
	producto = models.ForeignKey('productos.Producto', on_delete = models.CASCADE)
	#borrar despues el argumento default
 	costo = models.DecimalField(max_digits=5, decimal_places=2, default = 1)
	cantidad = models.IntegerField(default = 1)

	def __str__(self):
		return str(self.producto.nombre)

	def __unicode__(self):
		return str(self.producto.nombre)

@receiver(post_save, sender=Compra_detalle)
def actualizar_stock_alamcen(instance, created, **kwargs):
	if created:
		almacen = Almacen()
		almacen.producto = instance.producto
		almacen.compra = instance.compra
		almacen.stock = instance.cantidad
		almacen.save()
