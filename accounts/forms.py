from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Perfil

class PerfilCreationForm(UserCreationForm):
    class Meta:
        model = Perfil
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar', 'direccion', 'pais', 'fecha_de_nacimiento')

class PerfilChangeForm(UserChangeForm):
    password = None  # opcional: ocultar campo password en form de edición
    class Meta:
        model = Perfil
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar', 'direccion', 'pais', 'fecha_de_nacimiento')
