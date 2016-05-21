"""celulares URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('home.urls', namespace = 'home')),
    url(r'^', include('usuarios.urls', namespace = 'usuarios')),
    url(r'^', include('clientes.urls', namespace = 'clientes')),
    url(r'^', include('proveedores.urls', namespace = 'proveedores')),
    url(r'^', include('productos.urls', namespace = 'productos')),
    url(r'^', include('ventas.urls', namespace = 'ventas')),
    url(r'^', include('compras.urls', namespace = 'ventas')),
    #url(r'^', include('apps.usuarios.urls', namespace = 'usuarios')),
    #url(r'^', include('apps.notas.urls', namespace = 'notas')),
    #url(r'^login/$', 'apps.usuarios.views.login'),
    #url(r'^', 'apps.clientes.views.home', name='home')
]
