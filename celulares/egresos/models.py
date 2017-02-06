from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Egreso(models.Model):
    descripcion = models.CharField(max_length=100, default="Detalle del egreso")
    monto = models.DecimalField(max_digits=7, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True, blank = True)

    def __str__(self):
        return self.descripcion

    def __unicode__(self):
        return self.descripcion
