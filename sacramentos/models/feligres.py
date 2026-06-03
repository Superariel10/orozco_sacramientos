from django.db import models


class Feligres(models.Model):
    nombres        = models.CharField(max_length=100)
    apellidos        = models.CharField(max_length=100)
    cedula            = models.CharField(max_length=20, unique=True)
    fecha_nacimiento   = models.DateField()
    lugar_nacimiento        = models.TextField()
    direccion = models.TextField()
    telefono   = models.CharField(max_length=20)
    email       = models.EmailField(unique=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'Feligres'
        verbose_name_plural = 'Feligreses'
        ordering            = ['nombres', 'apellidos']

    def __str__(self):
        return self.nombres + ' ' + self.apellidos