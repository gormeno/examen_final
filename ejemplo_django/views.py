from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Mi primeras aplicacion web')

def hola(request):
    return HttpResponse('Esta es la ruta hola')

def hastaLuego(request):
    return HttpResponse('Hasta luego amigos')