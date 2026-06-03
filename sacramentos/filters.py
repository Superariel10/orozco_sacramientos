import django_filters
from sacramentos.models import Sacramento, Feligres , RegistroSacramento, Padrinos, CursoSacramental


class SacramentoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model  = Sacramento
        fields = ['nombre']

class FeligresFilter(django_filters.FilterSet):
    nombres = django_filters.CharFilter(lookup_expr='icontains')
    apellidos = django_filters.CharFilter(lookup_expr='icontains')
    cedula = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model  = Feligres
        fields = ['nombres', 'apellidos', 'cedula']

class RegistroSacramentoFilter(django_filters.FilterSet):
    sacerdote = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = RegistroSacramento
        fields = ['sacerdote']

class PadrinosFilter(django_filters.FilterSet):
    feligres = django_filters.ModelChoiceFilter(
        queryset=Feligres.objects.all()
    )
    sacramento = django_filters.ModelChoiceFilter(
        queryset=Sacramento.objects.all()
    )

    class Meta:
        model = Padrinos
        fields = ['feligres', 'sacramento']

class CursoSacramentalFilter(django_filters.FilterSet):
    nombre_curso = django_filters.CharFilter(lookup_expr='icontains')

    feligres = django_filters.ModelChoiceFilter(
        queryset=Feligres.objects.all()
    )

    sacramento = django_filters.ModelChoiceFilter(
        queryset=Sacramento.objects.all()
    )

    class Meta:
        model = CursoSacramental
        fields = ['nombre_curso']