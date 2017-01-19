from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^categorias/agregar$', agregarcategoria.as_view(), name="categorias"),
	url(r'^categorias/agregar-ajax$', agregarcategorias, name="agregar-categorias"),
	url(r'^precios/agregar$', precios.as_view(), name="precios"),
	url(r'^precios/agregar-ajax$', agregarprecios, name="agregar-precios"),
	#url(r'^productos/agregar$', agregarproducto.as_view(), name="productos"),
	url(r'^productos/agregar$', agregarproducto, name="productos"),
	url(r'^productos/agregar-ajax$', agregarproductos, name="productos"),
	url(r'^productos/buscar-ajax$', buscarproductos, name="buscarproductos"),
	url(r'^productos/buscar-ajax2$', buscarproductos2, name="buscarproducto2"),
	url(r'^productos/editar-ajax$', editarproductos, name="productos"),
	url(r'^almacen/buscar$', buscaralmacen.as_view(), name="buscaralmacens"),
	url(r'^almacen/buscar-ajax2$', buscaralmacen2, name="buscaralmacens"),
	url(r'^almacen/buscar-ajax$', buscarproductos3, name="buscarproducto3"),
	url(r'^productos/buscar$', buscarproducto.as_view(), name="buscarproducto"),
	url(r'^categorias/buscar$', buscarcategoria.as_view(), name="categorias"),
	url(r'^categorias/buscar-ajax$', buscarcategorias, name="buscarcategorias"),
	url(r'^categorias/editar-ajax$', editarcategorias, name="buscarcategorias"),
	url(r'^precios/buscar$', buscarprecio.as_view(), name="precios"),
	url(r'^precios/buscar-ajax$', buscarprecios, name="buscarprecios"),
	url(r'^precios/editar-ajax$', editarprecios, name="editarprecios"),
	url(r'^precios/buscar2-ajax$', buscarprecios2, name="buscarprecios2"),
	url(r'^productos/editar/(?P<term>[0-9]+)/$', editarproducto, name="editarproducto"),
	url(r'^precios/editar/(?P<term>[0-9]+)/$', editarprecio, name="editarprecio"),
	url(r'^categorias/editar/(?P<term>[0-9]+)/$', editarcategoria, name="editarcategoria"),
]
