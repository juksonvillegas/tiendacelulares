from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from proveedores.models import Proveedor
from productos.models import Producto
from django.http import HttpResponse
from .models import Compra, Compra_detalle
import json
from django.template import RequestContext

# Create your views here.
@method_decorator(login_required,name='dispatch')
class agregarcompra(TemplateView):
	template_name= 'compras/agregar.html'

@login_required(login_url='/')
def agregarcompras(request):
	if request.method == 'POST':
		try:
			campo = 'Debe ingresar Proveedor'
			cproveedor = int(request.POST.get('proveedor'))
			campo = 'Error en el tipo de documentacion de Venta'
			print(request.POST.get('documentado'))
			ccdocumentado = bool(request.POST.get('documentado'))
			proveedor = Proveedor.objects.get(id = cproveedor)
			compra = Compra(proveedor = proveedor, documentado = ccdocumentado)
			lista = request.POST.getlist('lista[]')
			compra.save()
			for li in lista:
				l = li.split(",")
				p = Producto.objects.get(id = int(l[0]))
				c = int(l[1])
				costo = l[2]
				cs = float(costo[4:])
				cd = Compra_detalle(compra=compra, producto=p, cantidad=c, costo=cs)
				cd.save()
			respuesta = "Compra registrada correctamente."
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
def listarcompras(request):
	try:
		compra = Compra.objects.filter(estado = True).order_by('-fecha')[:10]
		total = 0
		detalle = []
		for c in compra:
			c.total = 0
			items = Compra_detalle.objects.filter(compra = c)
			for i in items:
				i.subtotal = i.cantidad * i.costo
				c.total += i.subtotal
				detalle.append(i)
		return render_to_response('compras/buscar.html', {'compras': compra, 'detalle':detalle}, context_instance=RequestContext(request))
	except Compra.DoesNotExist:
		return render_to_response('ventas/buscar.html', context_instance=RequestContext(request))
