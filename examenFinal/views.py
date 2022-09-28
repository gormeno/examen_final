from datetime import datetime
from django.shortcuts import render
from django.urls import reverse
from .models import tareasExamen, usuariosFinal
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        passwordUsuario = request.POST.get('passwordUsuario')
        #Validacion de informacion
        usuario_registrado = 0
        usuarios_totales = usuariosFinal.objects.all()

        for usuario in usuarios_totales:
            if usuario.usuario == nombreUsuario and usuario.contra == passwordUsuario:
                usuario_registrado = 1
        
        if usuario_registrado == 1:
            return HttpResponseRedirect(reverse('examenFinal:dashboard'))
        else:
            return render(request,'examenFinal/ingresar.html',{
                'mensaje':'Los datos ingresados son incorrectos',
            })
    return render(request,'examenFinal/ingresar.html')

def dashboard(request):
    fecha_minima = str(datetime.today().date()) # para controlar la fecha de creación de tarea y la edición de la fecha de entrega
    return render(request,'examenFinal/dashboard.html',{
        'tareas_totales':tareasExamen.objects.all().order_by('id'),
        'fecha_minima':fecha_minima 
    })

def datosTarea(response,id_tarea): # Pregunta 1-1: permite devolver la información de los parámetros de una tarea como un objeto JSON
    tarea_filtro = tareasExamen.objects.filter(id=id_tarea)
    tarea = tarea_filtro[0]
    return JsonResponse({
        'tarea' :{
            'fechaCreacion':tarea.fechaCreacion,
            'fechaEntrega':tarea.fechaEntrega,
            'descripcion':tarea.descripcion,
            'estadoTarea':tarea.estadoTarea
        }
    })

def crearTarea(response,descripcion,fechaEntrega):
    tareasExamen(fechaEntrega=fechaEntrega,descripcion=descripcion).save()
    tareas_totales = tareasExamen.objects.all()
    tareas_info = []
    for tarea in tareas_totales:
        tareas_info.append([tarea.id,tarea.fechaCreacion,tarea.fechaEntrega,tarea.descripcion,tarea.estadoTarea])
    return JsonResponse({
        'tareas':tareas_info,
    })

    # return JsonResponse({
    #     'info':'RegistroOK'
    # })

def cargarTareas(response):
    tareas_totales = tareasExamen.objects.all()
    tareas_info = []
    for tarea in tareas_totales:
        tareas_info.append([tarea.id,tarea.fechaCreacion,tarea.fechaEntrega,tarea.descripcion,tarea.estadoTarea])
    return JsonResponse({
        'tareas':tareas_info,
    })

def eliminarTarea(response,id_tarea):
    tarea_a_eliminar = tareasExamen.objects.filter(id=id_tarea)
    tarea_a_eliminar.delete()
    return HttpResponse('EliminadoOK')