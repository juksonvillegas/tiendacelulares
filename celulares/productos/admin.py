from django.contrib import admin
from .models import Categoria, Precio, Producto

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Precio)
admin.site.register(Producto)
#admin.site.register(Almacen)
