from django.db import models

from sacramentos.models.registro_sacramento import RegistroSacramento

class Padrinos(models.Model):
    registro_sacramento    = models.ForeignKey(
        RegistroSacramento,
        on_delete=models.PROTECT,
        related_name='padrinos',
    )
    nombres   = models.CharField()
    apellidos        = models.CharField()
    cedula = models.CharField()
    telefono   = models.CharField()
    parentesco   = models.CharField()
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'Padrino'
        verbose_name_plural = 'Padrinos'
        ordering            = ['nombres']

    def __str__(self):
        return self.nombres