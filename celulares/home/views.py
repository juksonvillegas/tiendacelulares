from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
# Create your views here.

###def principal(request):
	###return render_to_response('index.html')

class principal(TemplateView):
	template_name = 'index.html'

def login(request):
	if not request.user.is_authenticated():
		print(request.user.is_authenticated())
		return render_to_response('login.html')
	else:
		return render_to_response('/consignaciones/buscar')

class preventa(TemplateView):
	template_name = 'preventa/preventa.html'
