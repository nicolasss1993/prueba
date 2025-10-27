from django.contrib import admin
from .models import Estudiante

#admin.site.register(Estudiante)

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    # columnas visibles en la lista del admin
    list_display = ('nombre', 'apellido', 'email', 'nro_legajo', 'fehca_de_nacimiento', 'fecha_de_creacion')

    # columnas con enlaces clickeables para entrar al detalle
    list_display_links = ('nombre', 'apellido')

    # campos por los que se puede buscar
    search_fields = ('nombre', 'apellido', 'email', 'nro_legajo')

    # filtros laterales
    list_filter = ('fecha_de_creacion', 'fehca_de_nacimiento')

    # orden por defecto
    ordering = ('apellido', 'nombre')

    # campos de solo lectura
    readonly_fields = ('fecha_de_creacion',)

    # organización de campos dentro del formulario de edición
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'apellido', 'email', 'nro_legajo', 'fehca_de_nacimiento')
        }),
        ('Metadatos', {
            'fields': ('fecha_de_creacion',),
            'classes': ('collapse',),
        }),
    )