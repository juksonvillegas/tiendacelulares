# -*- encoding: utf-8 -*-
from .models import Usuario
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import json

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

@login_required(login_url='/')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

@method_decorator(login_required, name='dispatch')
class agregarusuario(TemplateView):
	template_name = 'usuarios/crear.html'

@login_required(login_url='/')
def listarusuarios(request):
    usuarios = Usuario.objects.all()
    return render_to_response('usuarios/lista.html', {'usuarios': usuarios}, context_instance=RequestContext(request))

@login_required(login_url='/')
def crearusuario(request):
    if request.method == 'POST':
        try:
            campo = 'Debe ingresar el nombre de usuario'
            nusuario = request.POST.get('usuario')
            campo = 'Debe ingresar el nombre de usuario'
            password = request.POST.get('password')
            campo = 'Debe ingresar un correo electronico valido'
            email = request.POST.get('email')
            campo = 'Debe ingresar nombres completo'
            nombre = request.POST.get('nombre')
            campo = 'Debe ingresar direccion'
            direccion = request.POST.get('direccion')
            campo = 'Debe ingresar numero de telefono'
            telefono = request.POST.get('telefono')
            campo = 'Debe ingresar url de la fotografia'
            foto = request.POST.get('foto')
            campo = 'No se obtuvo is_staff'
            admin = request.POST.get('administrador')
            if admin == 'true':
                is_staff = True
            else:
                is_staff = False
            usuario = Usuario()
            usuario.usuario = nusuario
            usuario.set_password(password)
            usuario.email = email
            usuario.nombre = nombre
            usuario.direccion = direccion
            usuario.telefono = telefono
            usuario.foto = foto
            usuario.is_staff = is_staff
            #usuario.save()
            respuesta = "Usuario registrado correctamente."
        except ValueError:
            respuesta = "Error: "
            respuesta =respuesta + campo
        except Exception as ex:
            respuesta = str(ex.message)
        finally:
            return HttpResponse(json.dumps(respuesta),content_type="application/json")
