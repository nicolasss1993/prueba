from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre_curso', 'comision', 'code', 'datetime_added')
    search_fields = ('nombre_curso', 'comision', 'code')
