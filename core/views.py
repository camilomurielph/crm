from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Cliente, Proyecto, Tarea, Enlace
from .forms import ClienteForm, ProyectoForm, TareaForm, EnlaceForm

@login_required
def index(request):
    return redirect('core:clientes')

# CLIENTES
@login_required
def cliente_lista(request):
    vista = request.GET.get('vista', 'tarjetas')
    clientes = Cliente.objects.all().prefetch_related('proyectos')
    return render(request, 'clientes/lista.html', {'clientes': clientes, 'vista': vista})

@login_required
def cliente_detalle(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'clientes/detalle.html', {'cliente': cliente})

@login_required
def cliente_crear(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/crear.html', {'form': form})

# PROYECTOS
@login_required
def proyecto_lista(request):
    vista = request.GET.get('vista', 'tarjetas')
    proyectos = Proyecto.objects.all().select_related('cliente')
    return render(request, 'proyectos/lista.html', {'proyectos': proyectos, 'vista': vista})

@login_required
def proyecto_detalle(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST' and request.FILES.get('contrato'):
        proyecto.contrato = request.FILES['contrato']
        proyecto.save()
        return redirect('core:proyecto_detalle', pk=proyecto.pk)
    return render(request, 'proyectos/detalle.html', {'proyecto': proyecto})

@login_required
def proyecto_crear(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES)
        cliente_id = request.POST.get('cliente')
        if form.is_valid() and cliente_id:
            proyecto = form.save(commit=False)
            proyecto.cliente_id = cliente_id
            proyecto.save()
            return redirect('core:proyectos')
    else:
        form = ProyectoForm()
    clientes = Cliente.objects.all()
    return render(request, 'proyectos/crear.html', {'form': form, 'clientes': clientes})

# TAREAS
@login_required
def tarea_lista(request, categoria=None):
    if categoria is None:
        categorias = ['actols', 'andres', 'camilo']
        data = {}
        for cat in categorias:
            total = Tarea.objects.filter(categoria=cat).count()
            completadas = Tarea.objects.filter(categoria=cat, completada=True).count()
            pendientes = total - completadas
            data[cat] = {'total': total, 'pendientes': pendientes, 'completadas': completadas}
        return render(request, 'tareas/lista.html', {'categorias': data})
    else:
        tareas = Tarea.objects.filter(categoria=categoria).order_by('completada', '-creada')
        mostrar_completadas = request.GET.get('mostrar_completadas', 'false') == 'true'
        if not mostrar_completadas:
            tareas = tareas.filter(completada=False)
        return render(request, 'tareas/lista_categoria.html', {
            'tareas': tareas,
            'categoria': categoria,
            'mostrar_completadas': mostrar_completadas,
        })

@login_required
def tarea_detalle(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    return render(request, 'tareas/detalle.html', {'tarea': tarea})

@login_required
def tarea_crear(request):
    categoria = request.GET.get('categoria', 'actols')
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            if 'categoria' in request.GET:
                tarea.categoria = request.GET['categoria']
            tarea.save()
            return redirect('core:tareas_categoria', categoria=tarea.categoria)
    else:
        form = TareaForm(initial={'categoria': categoria})
    return render(request, 'tareas/crear.html', {'form': form, 'categoria': categoria})

@login_required
def tarea_editar(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('core:tarea_detalle', pk=tarea.pk)
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tareas/editar.html', {'form': form, 'tarea': tarea})

@login_required
def tarea_eliminar(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        categoria = tarea.categoria
        tarea.delete()
        return redirect('core:tareas_categoria', categoria=categoria)
    return render(request, 'tareas/confirmar_eliminar.html', {'tarea': tarea})

@login_required
def tarea_toggle(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        tarea.completada = not tarea.completada
        tarea.save()
        return render(request, 'tareas/_tarea_item.html', {'tarea': tarea})
    return HttpResponse(status=405)

# ENLACES
@login_required
def enlace_lista(request):
    enlaces = Enlace.objects.all()
    return render(request, 'enlaces/lista.html', {'enlaces': enlaces})

@login_required
def enlace_crear(request):
    if request.method == 'POST':
        form = EnlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:enlaces')
    else:
        form = EnlaceForm()
    return render(request, 'enlaces/crear.html', {'form': form})

@login_required
def enlace_editar(request, pk):
    enlace = get_object_or_404(Enlace, pk=pk)
    if request.method == 'POST':
        form = EnlaceForm(request.POST, instance=enlace)
        if form.is_valid():
            form.save()
            return redirect('core:enlaces')
    else:
        form = EnlaceForm(instance=enlace)
    return render(request, 'enlaces/editar.html', {'form': form, 'enlace': enlace})

@login_required
def enlace_eliminar(request, pk):
    enlace = get_object_or_404(Enlace, pk=pk)
    if request.method == 'POST':
        enlace.delete()
        return redirect('core:enlaces')
    return render(request, 'enlaces/confirmar_eliminar.html', {'enlace': enlace})
