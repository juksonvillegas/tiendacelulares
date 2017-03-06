from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext
import json
import barcode
from .models import Egreso
from django.db.models import Q
from django.core import serializers
from django.db.models import Sum
from datetime import date

# Create your views here.
@method_decorator(login_required, name='dispatch')
class agregaregreso(TemplateView):
	template_name = 'egresos/agregar.html'

@login_required(login_url='/')
def agregaregresos(request):
    if request.method == 'POST':
        try:
            campo = 'Debe ingresar descripcion'
            descripcion = request.POST.get('descripcion')
            monto = float(request.POST.get('monto'))
            egreso = Egreso(descripcion = descripcion, monto = monto)
            egreso.save()
            respuesta = "Egreso registrado correctamente."
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
def listaregresos(request):
	try:
		egresos = Egreso.objects.filter(fecha__date = date.today()).order_by('-fecha')
		return render_to_response('egresos/listar.html', {'egresos':egresos}, context_instance=RequestContext(request))
	except Venta.DoesNotExist:
		return render_to_response('egresos/listar.html', context_instance=RequestContext(request))
