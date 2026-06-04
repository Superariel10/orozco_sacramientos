from django.db import models

from sacramentos.models.sacramento import Sacramento
from sacramentos.models.feligres import Feligres

class RegistroSacramento(models.Model):
    sacramento    = models.ForeignKey(
        Sacramento,
        on_delete=models.PROTECT,
        related_name='registro_sacramentos',
    )
    feligres    = models.ForeignKey(
        Feligres,
        on_delete=models.PROTECT,
        related_name='registro_sacramentos_feligreses',
    )
    fecha_sacramento   = models.DateField()
    lugar        = models.TextField()
    sacerdote = models.CharField()
    numero_acta = models.CharField(unique=True)
    libro   = models.CharField()
    folio   = models.CharField()
    observaciones = models.TextField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'Registro_sacramento'
        verbose_name_plural = 'Registro_sacramentos'
        ordering            = ['sacerdote', 'feligres', 'sacramento']

    def __str__(self):
        return self.sacerdote