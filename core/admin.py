from django.contrib import admin
from .models import Cliente, Proyecto, Tarea, Enlace

admin.site.register(Cliente)
admin.site.register(Proyecto)
admin.site.register(Tarea)
admin.site.register(Enlace)
