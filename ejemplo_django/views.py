from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

informacion_usuarios = [['Alexander','Segovia'],['Javier','Hilario'],['Martin','Leyva']]
# Create your views here.

def index(request):
    return HttpResponse('Mi primera aplicacion web')

def hola(request):
    lista_elementos = ['Python','Django','Flask','Javascript','Docker']
    return render(request,'ejemplo_django/hola.html',{
        'lista_elementos':lista_elementos,
    })

def hastaLuego(request): 
    return render(request,'ejemplo_django/hastaLuego.html')

def usuarioInfo(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('usuarioNombre')
        apellidoUsuario = request.POST.get('usuarioApellido')
        informacion_usuarios.append([nombreUsuario,apellidoUsuario])
        return render(request,'ejemplo_django/usuariosInfo.html',{
            'informacion_usuarios':informacion_usuarios,
        })
    return render(request,'ejemplo_django/usuariosInfo.html',{
        'informacion_usuarios':informacion_usuarios,
    })
