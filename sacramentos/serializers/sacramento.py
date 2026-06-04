from rest_framework import serializers
from django.utils.text import slugify
from sacramentos.models import Sacramento


class SacramentoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Sacramento
        fields = [
            'id', 'nombre', 'descripcion',
            'requiere_padrinos', 'requiere_curso', 'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def validate_nombre(self, value):
        qs = Sacramento.objects.filter(nombre__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('A sacramento with this name already exists.')
        return value