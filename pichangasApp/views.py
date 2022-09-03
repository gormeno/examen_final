from django.shortcuts import render
from pichangasApp.models import usuarios_app
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def ingresar(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        passwordUsuario = request.POST.get('passwordUsuario')
        #Validacion de informacion
        usuario_registrado = 0
        usuarios_totales = usuarios_app.objects.all()

        for usuario in usuarios_totales:
            if usuario.nombre == nombreUsuario and usuario.psw_usuario == passwordUsuario:
                usuario_registrado = 1
        
        if usuario_registrado == 1:
            return HttpResponseRedirect(reverse('pichangasApp:dashboard'))
        else:
            return render(request,'pichangasApp/ingresar.html',{
                'mensaje':'Los datos ingresados son incorrectos',
            })
    return render(request,'pichangasApp/ingresar.html')

def dashboard(request):
    return render(request,'pichangasApp/dashboard.html')