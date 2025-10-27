from django.db import models
import uuid

class Curso(models.Model):
    nombre_curso = models.CharField(max_length=200)
    datetime_added = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=32, default=uuid.uuid4().hex, unique=True)
    comision = models.IntegerField(unique=True)

    class Meta:
        permissions = [
            ("ver_cursos_detail", "Puede ver el detalle del curso"),
        ]
    

    def __str__(self):
        return f"{self.nombre_curso} (Comisión {self.comision})"
