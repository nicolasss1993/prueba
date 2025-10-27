from django.urls import path
from .views import index, crear_estudiante, lista_estudiantes, ver_estudiante, editar_estudiante, eliminar_estudiante

urlpatterns = [
    path("", index, name="index"),
    path('estudiantes/nuevo/', crear_estudiante, name='estudiante_form'),
    path('estudiantes/', lista_estudiantes, name='estudiante_list'),
    path('estudiantes/<int:pk>/', ver_estudiante, name='estudiante_detail'),
    path('estudiantes/<int:pk>/editar/', editar_estudiante, name='estudiante_edit'),
    path('estudiantes/<int:pk>/eliminar/', eliminar_estudiante, name='estudiante_delete'),
]
