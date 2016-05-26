from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Cliente
from django.core import serializers
from django.db.models import Q
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json
from datetime import datetime
import time


class home(TemplateView):
	template_name = 'index.html'

@login_required(login_url='/')
def listarclientes(request):
	clients = Cliente.objects.all()
	user = request.user
	return render_to_response('clientes/buscar.html', {'clients': clients}, context_instance=RequestContext(request))

@login_required(login_url='/')
def buscarcliente(request):
	if request.is_ajax():
		texto = request.GET['term']
		if texto is not None:
			clients = Cliente.objects.filter(Q(nombre__contains = texto) | Q(email__contains = texto) |	Q(dni__contains = texto))
			lista = []
			if texto == 'listar':
				clients = Cliente.objects.all().order_by('nombre')
			for c in clients:
				lista.append({'id':c.id, 'dni':c.dni, 'nombre':c.nombre, 'nacimiento':str(c.nacimiento), 'sexo':c.sexo, 'direccion':c.direccion, 'email':c.email, 'telefono':c.telefono, 'mayorista':c.mayorista})
			data = json.dumps(lista)
			return HttpResponse(data, content_type='application/json')

@login_required(login_url='/')
def buscarcliente2(request):
	if request.is_ajax():
		texto = request.GET['term']
		print(texto)
		if texto is not None:
			clientes = Cliente.objects.filter(Q(nombre__contains = texto), mayorista = True)[:10]
			results = []
			for cliente in clientes:
				cliente_json = {}
				cliente_json['id'] = cliente.id
				cliente_json['label'] = cliente.nombre
				cliente_json['value'] = cliente.nombre
				results.append(cliente_json)
			data = json.dumps(results)
			return HttpResponse(data, content_type="application/json")

@login_required(login_url='/')
def buscarcliente3(request):
	if request.is_ajax():
		texto = request.GET['term']
		print(texto)
		if texto is not None:
			clientes = Cliente.objects.filter(Q(nombre__contains = texto))[:10]
			results = []
			for cliente in clientes:
				cliente_json = {}
				cliente_json['id'] = cliente.id
				cliente_json['label'] = cliente.nombre
				cliente_json['value'] = cliente.nombre
				results.append(cliente_json)
			data = json.dumps(results)
			return HttpResponse(data, content_type="application/json")

@method_decorator(login_required, name='dispatch')
class agregarcliente(TemplateView):
	template_name = 'clientes/agregar.html'

@login_required(login_url='/')
def agregarclientes(request):
	if request.method == 'POST':
		try:
			campo = "Debe ingresar un dni."
			dni = str(int(request.POST.get('dni')))
			campo = "Debe ingresar un nombre."
			nombre = request.POST.get('nombre')
			campo = "Debe ingresar una fecha correcta."
			nac = request.POST.get('nacimiento')
			nacimiento = datetime.strptime(nac , '%d-%m-%Y')
			campo = "Sexo"
			sexo = bool(int(request.POST.get('sexo')))
			campo = "Direccion"
			direccion = request.POST.get('direccion')
			campo = "email"
			email = request.POST.get('email')
			campo = "telefono"
			telefono = request.POST.get('telefono')
			campo = "Es mayorista"
			esmayorista = request.POST.get('puntoventa')
			if esmayorista == 'true':
				mayorista = True
			else:
				mayorista = False
			if dni != '' and nombre != '' and direccion != '' and telefono != '':
				cliente = Cliente()
				cliente.dni = dni
				cliente.nombre = nombre
				cliente.nacimiento = nacimiento
				cliente.sexo = sexo
				cliente.direccion = direccion
				cliente.email = email
				cliente.telefono = telefono
				cliente.mayorista = mayorista
				cliente.save()
				respuesta = "Cliente registrado correctamente."
			else:
				respuesta = "Debe ingresar todos los datos."
		except ValueError:
			respuesta = "Error: "
			respuesta =respuesta + campo
		except Exception as ex:
			respuesta = str(ex.message)
			print(type(ex).__name__)
		finally:
			return HttpResponse(
				json.dumps(respuesta),
				content_type="application/json"
			)

@login_required(login_url='/')
def editarcliente(request, client):
	cliente = Cliente.objects.get(id = client)
	return render_to_response('clientes/editar.html', {'cliente': cliente}, context_instance=RequestContext(request))
