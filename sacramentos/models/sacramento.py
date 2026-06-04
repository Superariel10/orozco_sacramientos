from django.db import models


class Sacramento(models.Model):
    nombre        = models.CharField(max_length=100, unique=True)
    descripcion        = models.TextField(unique=True)
    requiere_padrinos = models.BooleanField(default=True)
    requiere_curso   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'Sacramento'
        verbose_name_plural = 'Sacramentos'
        ordering            = ['nombre']

    def __str__(self):
        return self.nombre