from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre_curso', 'comision']
        widgets = {
            'nombre_curso': forms.TextInput(attrs={'class': 'form-control'}),
            'comision': forms.NumberInput(attrs={'class': 'form-control'}),
        }

