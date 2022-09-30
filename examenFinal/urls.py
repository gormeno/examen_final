from . import views
from django.urls import path

app_name = 'examenFinal'

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('datosTarea/<str:id_tarea>',views.datosTarea,name='datosTarea'),
    path('crearTarea/<str:descripcion>/<str:fechaEntrega>',views.crearTarea,name='crearTarea'),
    path('cargarTareas',views.cargarTareas,name='cargarTareas'),
    path('eliminarTarea/<str:id_tarea>',views.eliminarTarea,name='eliminarTarea'),
    path('editarTarea',views.editarTarea,name='editarTarea'),
]