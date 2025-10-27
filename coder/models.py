from django.db import models
from cursos.models import Curso


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    nro_legajo = models.IntegerField(unique=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fehca_de_nacimiento = models.DateField(null=True)
    curso = models.ForeignKey(
        Curso,
        on_delete=models.SET_NULL,  # Si se borra el curso, el estudiante queda sin curso
        null=True,
        blank=True,
        related_name='estudiantes'  # Permite acceder a estudiantes desde Curso
    )

    def __str__(self):
        return f"Estudiante: {self.nombre} - Nro Legajo: {self.nro_legajo}"


class Examenes(models.Model):
    nota = models.FloatField()
    asignatura = models.CharField(max_length=30)
    nombre_de_estudiante = models.CharField(max_length=100)

# class Asignatura(models.Model):
#     nombre = models.CharField(max_length=100)
#     codigo = models.CharField(max_length=100, unique=True)