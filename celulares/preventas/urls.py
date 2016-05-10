from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^preventas/agregar$', agregarpreventa.as_view(), name="agregarpreventa"),
	url(r'^preventas/agregar2$', agregarpreventa2.as_view(), name="agregarpreventa"),
	url(r'^preventas/buscar$', listarpreventas, name="listarpreventas"),
	url(r'^preventas/agregar-ajax$', agregarpreventas, name="agregarpreventas"),
	url(r'^preventas/editar/(?P<term>\d+)$', devolverpreventa, name='detalle'),
]