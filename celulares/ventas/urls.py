from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^consignaciones/agregar$', agregarconsignacion.as_view(), name="agregarconsignacion"),
	url(r'^ventas/agregar$', agregarventa.as_view(), name="agregarventa"),
	url(r'^consignaciones/buscar$', listarconsignaciones, name="listarconsignacion"),
	url(r'^consignaciones/agregar-ajax$', agregarconsignaciones, name="agregarconsignaciones"),
	url(r'^consignaciones/retornar/(?P<term>[0-9]+)/$', retornarconsignaciones, name="retornarconsignaciones"),
	url(r'^consignaciones/eliminar/(?P<term>[0-9]+)/$', eliminarconsignacion, name="eliminarconsignacion"),
	url(r'^ventas/agregar-ajax$', agregarventas, name="agregarventas"),
]
