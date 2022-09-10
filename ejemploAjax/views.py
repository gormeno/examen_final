from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    return render(request,'ejemploAjax/index.html')

def cargarInformacion(request,num):
    if num == '1':
        return HttpResponse('Texto 1 del servidor')
    else:
        return HttpResponse('Texto del servidor, no se recibio 1')

def cargarInfoUsuario(request):
    return JsonResponse({
        'usuario_1' :{
            'nombre':'alexander',
            'apellido':'segovia',
            'edad':'25',  
        },
        'usuario_2' :{
            'nombre':'javier',
            'apellido':'hilario',
            'edad':'35',
        }      
    })