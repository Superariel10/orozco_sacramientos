from rest_framework import serializers
from django.utils.text import slugify
from sacramentos.models import CursoSacramental

class CursoSacramentalSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CursoSacramental
        fields = [
            'id', 'feligres','sacramento', 'nombre_curso', 'fecha_inicio', 'fecha_fin', 'estado', 'responsable', 'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def validate_feligres(self, value):
        qs = CursoSacramental.objects.filter(feligres=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('A curso with this name already exists.')
        return value