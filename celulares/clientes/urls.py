"""mipymecelulares URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^$', home.as_view(), name="index"),
	url(r'^clientes/buscar$', listarclientes, name="listarclientes"),
	url(r'^clientes/agregar$', agregarcliente.as_view(), name="agregarclientes"),
	url(r'^clientes/buscar-ajax$', buscarcliente, name="buscarclientes"),
    url(r'^clientes/buscar-ajax2$', buscarcliente2, name="buscarclientes2"),
    url(r'^clientes/agregar-ajax$', agregarclientes, name="agregarcliente"),
    url(r'^clientes/editar/(?P<client>[0-9]+)/$', editarcliente, name="editarcliente"),

]
