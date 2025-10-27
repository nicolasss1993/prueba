from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

def avatar_upload_to(instance, filename):
    return f'avatars/{instance.username}/{filename}'

class Perfil(AbstractUser):
    avatar = models.ImageField(
        upload_to=avatar_upload_to,
        default='default/perfil/default.png',
        verbose_name=_('Avatar'),
        blank=True,
        null=True
    )
    direccion = models.CharField(_('Dirección'), max_length=255, blank=True)
    pais = models.CharField(_('País'), max_length=100, blank=True)
    fecha_de_nacimiento = models.DateField(_('Fecha de nacimiento'), blank=True, null=True)

    class Meta:
        verbose_name = _('Perfil')
        verbose_name_plural = _('Perfiles')

    def __str__(self):
        return self.get_full_name() or self.username
