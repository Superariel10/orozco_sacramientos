from rest_framework import serializers
from django.utils.text import slugify
from sacramentos.models import Feligres


class FeligresSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Feligres
        fields = [
            'id', 'nombres', 'apellidos', 'cedula', 'fecha_nacimiento',
            'lugar_nacimiento', 'direccion', 'telefono', 'email', 'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def validate_nombres(self, value):
        qs = Feligres.objects.filter(nombres__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('A feligres with this name already exists.')
        return value