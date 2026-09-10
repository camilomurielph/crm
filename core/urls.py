from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),

    # CLIENTES
    path('clientes/', views.cliente_lista, name='clientes'),
    path('clientes/nuevo/', views.cliente_crear, name='cliente_crear'),
    path('clientes/<int:pk>/', views.cliente_detalle, name='cliente_detalle'),

    # PROYECTOS
    path('proyectos/', views.proyecto_lista, name='proyectos'),
    path('proyectos/nuevo/', views.proyecto_crear, name='proyecto_crear'),
    path('proyectos/<int:pk>/', views.proyecto_detalle, name='proyecto_detalle'),

    # TAREAS — Rutas específicas primero, las genéricas después
    path('tareas/', views.tarea_lista, name='tareas'),
    path('tareas/crear/', views.tarea_crear, name='tarea_crear'),
    path('tareas/<int:pk>/', views.tarea_detalle, name='tarea_detalle'),
    path('tareas/<int:pk>/editar/', views.tarea_editar, name='tarea_editar'),
    path('tareas/<int:pk>/eliminar/', views.tarea_eliminar, name='tarea_eliminar'),
    path('tareas/<int:pk>/toggle/', views.tarea_toggle, name='tarea_toggle'),
    path('tareas/<slug:categoria>/', views.tarea_lista, name='tareas_categoria'),

    # ENLACES
    path('enlaces/', views.enlace_lista, name='enlaces'),
    path('enlaces/crear/', views.enlace_crear, name='enlace_crear'),
    path('enlaces/<int:pk>/editar/', views.enlace_editar, name='enlace_editar'),
    path('enlaces/<int:pk>/eliminar/', views.enlace_eliminar, name='enlace_eliminar'),
]
