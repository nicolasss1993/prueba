from django.urls import path
from .views import (
    CursoListView, CursoCreateView, CursoUpdateView,
    CursoDetailView, CursoDeleteView
)

urlpatterns = [
    path('', CursoListView.as_view(), name='curso_list'),
    path('nuevo/', CursoCreateView.as_view(), name='curso_create'),
    path('<str:code>/', CursoDetailView.as_view(), name='curso_detail'),
    path('<str:code>/editar/', CursoUpdateView.as_view(), name='curso_edit'),
    path('<str:code>/eliminar/', CursoDeleteView.as_view(), name='curso_delete'),
]