from __future__ import unicode_literals

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.db import models
from productos.models import Almacen

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

@receiver(post_save, sender=Venta_detalle)
def actualizar_stock_alamcen(instance, created, **kwargs):
	if created:
		cantidad = instance.cantidad
		items = Almacen.objects.filter(producto=instance.producto)
		print("se capturo items de almacen")
		for i in items:
			if cantidad > 0:
				if cantidad > i.stock:
					print("cantidad mayor que producto")
					cantidad -= i.stock
					i.stock = 0
					print("item estado false")
				else:
					print("cantidad menor o igual a producto")
					i.stock -=cantidad
					print("se resto la cantidad")
					cantidad = 0
				if i.stock == 0:
					print("producto desactivado")
					i.estado = False
				i.save()

@receiver(post_delete, sender=Venta_detalle)
def retornar_stock_almacen(instance, deleted, **kwargs):
	if deleted:
		item = Almacen.objects.get(producto = instance.producto)
		print('Se obtuvo el ultimo item eliminado')
		item.stock += instance.cantidad
		item.save()
