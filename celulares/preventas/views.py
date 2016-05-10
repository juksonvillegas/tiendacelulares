from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json
from django.http import HttpResponse
from django.template import RequestContext
from productos.models import Producto
from clientes.models import Cliente
from .models import Preventa
from django.shortcuts import get_object_or_404


# Create your views here.
@method_decorator(login_required, name='dispatch')
class agregarpreventa(TemplateView):
	template_name = 'preventas/agregar.html'

@method_decorator(login_required, name='dispatch')
class agregarpreventa2(TemplateView):
	template_name = 'preventas/agregar2.html'

@login_required(login_url='/')
def listarpreventas(request):
	preventas = Preventa.objects.filter(estado=True).order_by('-fecha')
	user = request.user 
	return render_to_response('preventas/buscar.html', {'preventas': preventas}, context_instance=RequestContext(request))


@login_required(login_url='/')
def agregarpreventas(request):
	if request.method == 'POST':
		try:
			campo = 'Debe ingresar un cliente'
			pcliente = int(request.POST.get('cliente'))
			campo = 'Debe ingresar un producto'
			pproducto = int(request.POST.get('producto'))
			campo = 'Debe ingresar una cantidad'
			pcantidad = int(request.POST.get('cantidad'))
			cliente = Cliente.objects.get(id = pcliente)
			producto = Producto.objects.get(id = pproducto)
			preventa = Preventa(cliente = cliente, producto = producto, cantidad = pcantidad)
			preventa.save()
			respuesta = "Preventa registrada correctamente."
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
def devolverpreventa(request, term):
	preventa = get_object_or_404(Preventa, pk = term)
	return render_to_response('preventas/editar.html', {'p': preventa}, context_instance=RequestContext(request))
