from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count

from sacramentos.models               import RegistroSacramento
from sacramentos.serializers.registro_sacramento import RegistroSacramentoSerializer
from sacramentos.permissions          import IsStaffOrReadOnly
from sacramentos.filters              import RegistroSacramentoFilter
from sacramentos.pagination           import StandardPagination

    
class RegistroSacramentoViewSet(viewsets.ModelViewSet):
    queryset           = RegistroSacramento.objects.all()
    serializer_class   = RegistroSacramentoSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class    = RegistroSacramentoFilter
    search_fields      = ['sacerdote','feligres__nombres', 'feligres__apellidos', 'sacramento__nombre']
    ordering_fields    = ['sacerdote', 'created_at']
    ordering           = ['sacerdote']

    @action(detail=True, methods=['get'], url_path='registro_sacramentos')
    def registro_sacramentos(self, request, pk=None):
        return Response([])

    @action(detail=False, methods=['get'], url_path='stats')
    def stats(self, request):
        qs = RegistroSacramento.objects.annotate(num_registros=Count('id', distinct=True))
        return Response({
            'total':    qs.count(),
            'detail': [
                {
                    'id':           c.id,
                    'sacerdote':         c.sacerdote,
                    'num_registros': c.num_registros,
                    'is_active':    c.is_active,
                }
                for c in qs.order_by('sacerdote')
            ],
        })