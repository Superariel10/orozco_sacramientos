from rest_framework import serializers
from django.utils.text import slugify
from sacramentos.models import RegistroSacramento

class RegistroSacramentoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = RegistroSacramento
        fields = [
            'id', 'feligres','sacramento', 'fecha_sacramento', 'lugar', 'sacerdote', 'numero_acta', 'libro', 'folio', 
            'observaciones', 'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def validate_feligres(self, value):
        qs = RegistroSacramento.objects.filter(feligres=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError(
                'Ya existe un registro para este feligrés.'
            )

        return value

