from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count

from sacramentos.models               import Feligres
from sacramentos.serializers.feligres import FeligresSerializer
from sacramentos.permissions          import IsStaffOrReadOnly
from sacramentos.filters              import FeligresFilter
from sacramentos.pagination           import StandardPagination


class FeligresViewSet(viewsets.ModelViewSet):
    queryset           = Feligres.objects.all()
    serializer_class   = FeligresSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class    = FeligresFilter
    search_fields      = ['nombres', 'apellidos', 'cedula']
    ordering_fields    = ['nombres', 'apellidos', 'created_at']
    ordering           = ['nombres', 'apellidos']

    @action(detail=True, methods=['get'], url_path='registro_sacramentos')
    def registro_sacramentos(self, request, pk=None):
        return Response([])

    @action(detail=False, methods=['get'], url_path='stats')
    def stats(self, request):
        qs = Feligres.objects.annotate(num_registros=Count('registro_sacramentos', distinct=True))
        return Response({
            'total':    qs.count(),
            'active':   qs.filter(is_active=True).count(),
            'inactive': qs.filter(is_active=False).count(),
            'detail': [
                {
                    'id':           c.id,
                    'name':         c.nombres + ' ' + c.apellidos,
                    'num_registros': c.num_registros,
                    'is_active':    c.is_active,
                }
                for c in qs.order_by('nombres', 'apellidos')
            ],
        })