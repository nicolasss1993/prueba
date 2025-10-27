from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Curso
from .forms import CursoForm

class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'cursos/curso_list.html'
    context_object_name = 'cursos'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Curso.objects.filter(nombre_curso__icontains=query).order_by('-datetime_added')
        return Curso.objects.all().order_by('-datetime_added')


class CursoCreateView(LoginRequiredMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/curso_form.html'
    success_url = reverse_lazy('curso_list')


class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/curso_form.html'
    success_url = reverse_lazy('curso_list')
    slug_field = 'code'
    slug_url_kwarg = 'code'


class CursoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Curso
    template_name = 'cursos/curso_detail.html'
    context_object_name = 'curso'
    slug_field = 'code'
    slug_url_kwarg = 'code'
    permission_required = 'cursos.ver_cursos_detail'


class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = 'cursos/curso_confirm_delete.html'
    success_url = reverse_lazy('curso_list')
    slug_field = 'code'
    slug_url_kwarg = 'code'
