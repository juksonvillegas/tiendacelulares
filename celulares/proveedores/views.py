from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Proveedor
from django.db.models import Q
from django.core import serializers
from django.http import HttpResponse
import json
# Create your views here.

@method_decorator(login_required, name='dispatch')
class listarproveedores(TemplateView):
	template_name = 'proveedores/buscar.html'

@login_required(login_url='/')
def buscarproveedor(request):
	if request.is_ajax():
		texto = request.GET['texto']
		if texto is not None:
			proveedores = Proveedor.objects.filter(nombre__contains = texto)
			data = serializers.serialize('json', proveedores, fields = {'ruc', 'nombre', 'direccion', 'telefono'})
			return HttpResponse(data, content_type='application/json')

@method_decorator(login_required, name='dispatch')
class agregarproveedor(TemplateView):
	template_name = 'proveedores/agregar.html'

@login_required(login_url='/')
def agregarproveedores(request):
	if request.method == 'POST':
		try:
			campo = "Debe ingresar un ruc correcto."
			ruc = str(int(request.POST.get('ruc')))
			campo = "Debe ingresar un nombre."
			nombre = request.POST.get('nombre')
			campo = "Debe ingresar una direccion."
			direccion = request.POST.get('direccion')
			campo = "Debe ingresar un telefono."
			telefono = request.POST.get('telefono')
			if ruc != '' and nombre != '' and direccion != '' and telefono != '':
				proveedor = Proveedor()
				proveedor.ruc = ruc 
				proveedor.nombre = nombre
				proveedor.direccion = direccion
				proveedor.telefono = telefono
				proveedor.save()
				respuesta = "Proveedor registrado correctamente."
			else:
				respuesta = 'Erorr:'
				respuesta = respuesta + campo
		except ValueError:
			respuesta = "Error: "
			respuesta =respuesta + campo  
		except Exception as ex:
			respuesta = str(ex.message)
		finally:
			return HttpResponse(
				json.dumps(respuesta), 
				content_type="application/json"
			)




