from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.template import RequestContext
import json
from .models import Consignacion, Consignacion_detalle, Venta, Venta_detalle
from django.http import HttpResponse
from clientes.models import Cliente
from productos.models import Producto


# Create your views here.
@method_decorator(login_required,name='dispatch')
class agregarconsignacion(TemplateView):
	template_name= 'ventas/consignacion/agregar.html'

@method_decorator(login_required,name='dispatch')
class agregarventa(TemplateView):
	template_name= 'ventas/agregar.html'

@login_required(login_url='/')
def agregarventas(request):
	if request.method == 'POST':
		try:
			campo = 'Debe ingresar cliente'
			ccliente = int(request.POST.get('cliente'))
			campo = 'Error en el tipo de documentacion de Venta'
			ccdocumentado = bool(request.POST.get('documentado'))
			cliente = Cliente.objects.get(id = ccliente)
			venta = Venta(cliente = cliente, documentado = ccdocumentado)
			lista = request.POST.getlist('lista[]')
			#consignacion.save()
			for li in lista:
				l = li.split(",")
				p = Producto.objects.get(id = int(l[0]))
				c = int(l[1])
				precio = l[2]
				pr = float(precio[4:])
				cd = Venta_detalle(venta=venta, producto=p, cantidad=c, precio=pr)
				#cd.save()
			respuesta = "Venta registrada correctamente."
		except ValueError as e:
			respuesta = str(e.message)
		except Exception as ex:
			respuesta = str(ex.message)
		finally:
			return HttpResponse(
				json.dumps(respuesta),
				content_type="application/json"
			)

@login_required(login_url='/')
def agregarconsignaciones(request):
	if request.method == 'POST':
		try:
			campo = 'Debe ingresar cliente'
			ccliente = int(request.POST.get('cliente'))
			cliente = Cliente.objects.get(id = ccliente)
			nota = str(request.POST.get('nota'))
			consignacion = Consignacion(cliente = cliente, nota= nota)
			lista = request.POST.getlist('lista[]')
			consignacion.save()
			for li in lista:
				l = li.split(",")
				cn = int(consignacion.pk)
				p = Producto.objects.get(id = int(l[0]))
				c=int(l[1])
				cd = Consignacion_detalle(consignacion=consignacion, producto=p, cantidad=c)
				cd.save()
			respuesta = "Consignacion registrada correctamente."
		except ValueError as e:
			respuesta = str(e.message)
		except Exception as ex:
			respuesta = str(ex.message)
		finally:
			return HttpResponse(
				json.dumps(respuesta),
				content_type="application/json"
			)

@login_required(login_url='/')
def listarconsignaciones(request):
	consig = Consignacion.objects.filter(estado = True).order_by('-fecha')
	detalle = Consignacion_detalle.objects.all()
	return render_to_response('ventas/consignacion/buscar.html', {'consigs': consig, 'detalle':detalle}, context_instance=RequestContext(request))

@login_required(login_url='/')
def retornarconsignaciones(request, term):
	consig = Consignacion.objects.get(id = term)
	consig.estado = False
	consig.save()
	return redirect('/consignaciones/buscar')

def eliminarconsignacion(request, term):
	consig = Consignacion.objects.get(id=term)
	consig.delete()
	return redirect('/consignaciones/buscar')
