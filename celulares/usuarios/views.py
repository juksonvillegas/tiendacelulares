# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect

def login(request):
    usuario = request.POST['usuario']
    password = request.POST['password']
    print(usuario, password)
    user = auth.authenticate(usuario=usuario, password=password)
    print user
    if user is not None and user.is_active:
        # Clave correcta, y el usuario está marcado "activo"
        auth.login(request, user)
        # Redirigir a una página de éxito.
        return HttpResponseRedirect('/consignaciones/buscar')
    else:
        # Mostrar una página de error
        print('desconocido')
        return HttpResponseRedirect("/")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

class home(TemplateView):
    template_name='usuarios/home.html'

class createuser(TemplateView):
    template_name = 'usuarios/create.html'
