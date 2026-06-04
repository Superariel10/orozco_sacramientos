from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count

from sacramentos.models               import CursoSacramental
from sacramentos.serializers.curso_sacramental import CursoSacramentalSerializer
from sacramentos.permissions          import IsStaffOrReadOnly
from sacramentos.filters              import CursoSacramentalFilter
from sacramentos.pagination           import StandardPagination

    
class CursoSacramentalViewSet(viewsets.ModelViewSet):
    queryset           = CursoSacramental.objects.all()
    serializer_class   = CursoSacramentalSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class    = CursoSacramentalFilter
    search_fields      = ['nombre_curso','feligres__nombres', 'feligres__apellidos', 'sacramento__nombre']
    ordering_fields    = ['nombre_curso', 'created_at']
    ordering           = ['nombre_curso']

    @action(detail=True, methods=['get'], url_path='curso_sacramental')
    def curso_sacramental(self, request, pk=None):
        return Response([])

    @action(detail=False, methods=['get'], url_path='stats')
    def stats(self, request):
        qs = CursoSacramental.objects.annotate(num_registros=Count('id', distinct=True))
        return Response({
            'total':    qs.count(),
            'detail': [
                {
                    'id':           c.id,
                    'nombre_curso':         c.nombre_curso,
                    'num_registros': c.num_registros,
                    'is_active':    c.is_active,
                }
                for c in qs.order_by('nombre_curso')
            ],
        })