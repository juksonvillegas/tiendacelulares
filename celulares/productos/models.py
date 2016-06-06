from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Categoria(models.Model):
	nombre = models.CharField(max_length = 35, blank = False)
	descripcion = models.CharField(max_length = 100, blank = False)

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre

class Precio(models.Model):
	punto = models.DecimalField(max_digits=5, decimal_places=2)
	cliente = models.DecimalField(max_digits=5, decimal_places=2)
	descripcion = models.CharField(max_length=100, default="Detalle del precio")

	def __str__(self):
		return self.descripcion

	def __unicode__(self):
		return self.descripcion

class Producto(models.Model):
	nombre = models.CharField(max_length = 100)
	categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE,)
	precio = models.ForeignKey('Precio', on_delete=models.CASCADE,)
	stock = models.IntegerField(default = 1)
	barras = models.CharField(max_length=13, blank=True)

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre

class Almacen(models.Model):
	producto = models.ForeignKey('Producto', on_delete=models.CASCADE,)
	stock = models.IntegerField()
	compra = models.ForeignKey('compras.Compra', on_delete=models.CASCADE,)
	estado = models.BooleanField(default = True)

	def __str__(self):
		return self.producto.nombre

	def __unicode__(self):
		return self.producto.nombre
