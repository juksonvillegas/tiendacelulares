from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^egresos/agregar$', agregaregreso.as_view(), name="egresos"),
	url(r'^egresos/agregar-ajax$', agregaregresos, name="agregar-egresos"),
]
