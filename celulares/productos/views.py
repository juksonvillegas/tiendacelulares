from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import RequestContext
import json
from .models import Categoria, Precio, Producto
import barcode
from django.db.models import Q
from django.core import serializers

# Create your views here.
@method_decorator(login_required, name='dispatch')
class agregarcategoria(TemplateView):
	template_name = 'productos/categoria_agregar.html'

@method_decorator(login_required, name='dispatch')
class buscarcategoria(TemplateView):
	template_name = 'productos/categoria_buscar.html'

@method_decorator(login_required, name='dispatch')
class precios(TemplateView):
	template_name = 'productos/precio_agregar.html'

@method_decorator(login_required, name='dispatch')
class buscarprecio(TemplateView):
	template_name = 'productos/precio_buscar.html'

@method_decorator(login_required, name='dispatch')
class buscarproducto(TemplateView):
	template_name = 'productos/buscar.html'

@login_required(login_url='/')
def buscarcategorias(request):
	if request.is_ajax():
		texto = request.GET['term']
		if texto is not None:
			categoria = Categoria.objects.filter(Q(nombre__contains = texto)| Q(descripcion__contains=texto))
			lista = []
			if texto == 'listar':
				categoria = Categoria.objects.all().order_by('nombre')
			for c in categoria:
				lista.append({'nombre':c.nombre, 'descripcion':c.descripcion})
			data = json.dumps(lista)
			return HttpResponse(data, content_type='application/json')

@login_required(login_url='/')
def buscarprecios(request):
	if request.is_ajax():
		texto = request.GET['term']
		if texto is not None:
			precio = Precio.objects.filter(Q(descripcion__contains=texto))
			lista = []
			if texto == 'listar':
				precio = Precio.objects.all().order_by('descripcion')
			for p in precio:
				lista.append({'descripcion':p.descripcion, 'punto': str(p.punto), 'cliente': str(p.cliente)})
			data = json.dumps(lista)
			return HttpResponse(data, content_type='application/json')

@login_required(login_url='/')
def buscarprecios2(request):
	if request.is_ajax():
		texto = request.GET['term']
		if texto is not None:
			p = Producto.objects.get(id = int(texto))
			results = {}
			results['punto'] = str(p.precio.punto)
			results['cliente'] = str(p.precio.cliente)
			data = json.dumps(results)
			return HttpResponse(data, content_type='application/json')

@login_required(login_url='/')
def buscarproductos(request):
	if request.is_ajax():
		texto = request.GET['term']
		if texto is not None:
			producto = Producto.objects.filter(Q(nombre__contains = texto)| Q(categoria__nombre__contains = texto) | Q(barras__contains = texto))
			lista = []
			if texto == 'listar':
				producto = Producto.objects.all().order_by('nombre')
			for p in producto:
				lista.append({'nombre':p.categoria.nombre + p.nombre , 'categoria':p.categoria.nombre,'preciopunto': str(p.precio.punto), 'preciocliente': str(p.precio.cliente) , 'stock':p.stock, 'barras':p.barras})
			data = json.dumps(lista)
			return HttpResponse(data, content_type='application/json')

@login_required(login_url='/')
def agregarproducto(request):
	categorias = Categoria.objects.all().order_by('nombre')
	precios = Precio.objects.all().order_by('descripcion')
	return render_to_response('productos/agregar.html', {'categorias':categorias, 'precios':precios}, context_instance=RequestContext(request))

@login_required(login_url='/')
def agregarcategorias(request):
	if request.method == 'POST':
		try:
			campo = 'Debe ingresar el nombre de la categoria'
			nombre = request.POST.get('nombre')
			campo = 'Debe ingresar una descripcion de la categoria'
			descripcion = request.POST.get('descripcion')
			categoria = Categoria()
			categoria.nombre = nombre
			categoria.descripcion = descripcion
			categoria.save()
			respuesta = "Categoria registrada correctamente."
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

@login_required(login_url='/')
def buscarproductos2(request):
	if request.is_ajax():
		texto = request.GET['term']
		if texto is not None:
			productos = Producto.objects.filter(Q(barras__contains = texto) | Q(nombre__contains = texto) | Q(categoria__nombre__contains = texto))[:10]
			results = []
			for producto in productos:
				producto_json = {}
				producto_json['id'] = producto.id
				producto_json['label'] = producto.categoria.nombre + " " + producto.nombre
				producto_json['value'] = producto.categoria.nombre + " " +producto.nombre
				results.append(producto_json)
			data = json.dumps(results)
			return HttpResponse(data, content_type="application/json")

@login_required(login_url='/')
def agregarproductos(request):
	if request.method == 'POST':
		try:
			campo = 'Debe seleccionar categoria'
			pcategoria = int(request.POST.get('categoria'))
			campo = 'Debe seleccionar precio'
			pprecio = int(request.POST.get('precio'))
			campo = 'Debe ingresar nombre para el producto'
			pnombre = request.POST.get('nombre')
			pcategoria = Categoria.objects.get(id = pcategoria)
			pprecio = Precio.objects.get(id = pprecio)
			producto = Producto(nombre = pnombre, categoria = pcategoria, precio = pprecio)
			producto.save()
			barra = str(producto.id).zfill(12)
			barra = barcode.get('ean13', barra)
			producto.barras = barra
			producto.save()
			respuesta = "Producto registrado correctamente."
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

@login_required(login_url='/')
def agregarprecios(request):
	if request.method == 'POST':
		try:
			campo = 'Debe ingresar el precio a cliente'
			cliente = float(request.POST.get('cliente'))
			campo = 'Debe ingresar el precio a punto de venta'
			punto = float(request.POST.get('punto'))
			campo = 'Debe ingresar la descripcion del precio'
			descripcion = request.POST.get('descripcion')
			precio = Precio()
			precio.cliente = cliente
			precio.punto = punto
			precio.descripcion = descripcion
			precio.save()
			respuesta = "Precio registrado correctamente."
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

@login_required(login_url='/')
def agregaralmacen(request):
	if request.method == 'POST':
		try:
			campo = 'Debe agregar producto'
			pproducto = int(request.POST.get('producto'))
			campo = 'Debe ingresar una cantidad'
			punto = int(request.POST.get('stock'))
			campo = 'Debe ingresar la descripcion del precio'
			descripcion = request.POST.get('descripcion')
			precio = Precio()
			precio.cliente = cliente
			precio.punto = punto
			precio.descripcion = descripcion
			precio.save()
			respuesta = "Precio registrado correctamente."
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
