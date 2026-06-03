from rest_framework import serializers
from django.utils.text import slugify
from sacramentos.models import Padrinos


class PadrinosSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Padrinos
        fields = [
            'id', 'registro_sacramento','nombres', 'apellidos', 'cedula', 'telefono', 'parentesco', 'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def validate_nombres(self, value):
        qs = Padrinos.objects.filter(nombres__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('A padrino with this name already exists.')
        return value