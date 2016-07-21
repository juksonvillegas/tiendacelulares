from django.contrib import admin
from .models import Consignacion, Consignacion_detalle, Venta, Venta_detalle
# Register your models here.
admin.site.register(Consignacion)
admin.site.register(Consignacion_detalle)
admin.site.register(Venta)
admin.site.register(Venta_detalle)
