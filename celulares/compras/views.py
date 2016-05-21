from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from proveedores.models import Proveedor
from productos.models import Producto
from django.http import HttpResponse

# Create your views here.
@method_decorator(login_required,name='dispatch')
class agregarcompra(TemplateView):
	template_name= 'compras/agregar.html'
