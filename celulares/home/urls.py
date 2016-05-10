from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^$', principal.as_view(), name="index"),
	url(r'^preventa/$', preventa.as_view(), name = "home"),
]
