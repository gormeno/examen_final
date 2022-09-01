from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

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