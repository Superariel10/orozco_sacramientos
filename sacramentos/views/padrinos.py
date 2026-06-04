from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count

from sacramentos.models               import Padrinos
from sacramentos.serializers.padrinos import PadrinosSerializer
from sacramentos.serializers.registro_sacramento import RegistroSacramentoSerializer
from sacramentos.permissions          import IsStaffOrReadOnly
from sacramentos.filters              import PadrinosFilter
from sacramentos.pagination           import StandardPagination

    
class PadrinosViewSet(viewsets.ModelViewSet):
    queryset           = Padrinos.objects.all()
    serializer_class   = PadrinosSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class    = PadrinosFilter
    search_fields      = ['nombres','apellidos', 'cedula', 'telefono', 'parentesco', 'registro_sacramento__sacerdote']
    ordering_fields    = ['nombres', 'created_at']
    ordering           = ['nombres']

    @action(detail=True, methods=['get'], url_path='registro_sacramentos')
    def registro_sacramentos(self, request, pk=None):
        return Response([])

    @action(detail=False, methods=['get'], url_path='stats')
    def stats(self, request):
        qs = Padrinos.objects.annotate(num_registros=Count('id', distinct=True))
        return Response({
            'total':    qs.count(),
            'active':   qs.filter(is_active=True).count(),
            'inactive': qs.filter(is_active=False).count(),
            'detail': [
                {
                    'id':           c.id,
                    'nombres':         c.nombres,
                    'num_registros': c.num_registros,
                    'is_active':    c.is_active,
                }
                for c in qs.order_by('nombres')
            ],
        })