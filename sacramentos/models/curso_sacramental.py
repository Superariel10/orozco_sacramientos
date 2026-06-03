from django.db import models

from sacramentos.models.sacramento import Sacramento
from sacramentos.models.feligres import Feligres

class CursoSacramental(models.Model):
    sacramento    = models.ForeignKey(
        Sacramento,
        on_delete=models.PROTECT,
        related_name='curso_sacramental',
    )
    feligres    = models.ForeignKey(
        Feligres,
        on_delete=models.PROTECT,
        related_name='curso_sacramental_feligreses',
    )
    nombre_curso   = models.CharField()
    fecha_inicio        = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField()
    responsable   = models.CharField()
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'CursoSacramental'
        verbose_name_plural = 'CursosSacramentales'
        ordering            = ['nombre_curso']

    def __str__(self):
        return self.nombre_curso