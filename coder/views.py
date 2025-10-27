from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante
from django.contrib.auth.decorators import login_required
from .forms import EstudianteForm
from django.urls import reverse
from django.contrib import messages


def index(request):
    return render(request, "coder/index.html")

@login_required
def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Estudiante creado correctamente.")
            return redirect('estudiante_list')
    else:
        form = EstudianteForm()
    
    return render(request, 'coder/estudiante_form.html', {'form': form})

@login_required
def lista_estudiantes(request):
    query = request.GET.get('q', '')
    if query:
        estudiantes = Estudiante.objects.filter(nombre__icontains=query).order_by('-fecha_de_creacion')
    else:
        estudiantes = Estudiante.objects.all().order_by('-fecha_de_creacion')
    
    return render(request, 'coder/estudiante_list.html', {'estudiantes': estudiantes, 'query': query})

@login_required
def ver_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'coder/estudiante_detail.html', {'estudiante': estudiante})

@login_required
def editar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            messages.success(request, "Estudiante modificado correctamente.")
            return redirect('estudiante_list')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'coder/estudiante_form.html', {'form': form, 'edicion': True})

@login_required
def eliminar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    estudiante.delete()
    messages.success(request, "Estudiante eliminado correctamente.")
    return redirect('estudiante_list')