from django.contrib import admin
from sacramentos.models import Sacramento
from sacramentos.models import Feligres
from sacramentos.models.padrinos import Padrinos
from sacramentos.models.registro_sacramento import RegistroSacramento
from sacramentos.models.curso_sacramental import CursoSacramental

@admin.register(Sacramento)
class SacramentoAdmin(admin.ModelAdmin):
    list_display        = ['id', 'nombre', 'descripcion','requiere_padrinos', 'requiere_curso', 'created_at']
    list_filter         = []
    search_fields       = ['nombre']
    prepopulated_fields = {}

@admin.register(Feligres)
class FeligresAdmin(admin.ModelAdmin):
    list_display        = ['id', 'nombres', 'apellidos', 'cedula', 'fecha_nacimiento', 'lugar_nacimiento', 'direccion', 'telefono', 'email', 'created_at']
    list_filter         = []
    search_fields       = ['nombres', 'apellidos', 'cedula']
    prepopulated_fields = {}

@admin.register(RegistroSacramento)
class RegistroSacramentoAdmin(admin.ModelAdmin):
    list_display        = ['id', 'feligres', 'sacramento', 'fecha_sacramento', 'lugar', 'sacerdote', 'numero_acta', 'libro', 'folio', 'observaciones', 'created_at']
    list_filter         = []
    search_fields       = ['sacerdote']
    prepopulated_fields = {}

@admin.register(Padrinos)
class PadrinosAdmin(admin.ModelAdmin):
    list_display        = ['id', 'nombres', 'apellidos', 'cedula', 'telefono', 'parentesco', 'created_at']
    list_filter         = []
    search_fields       = ['nombres']
    prepopulated_fields = {}

@admin.register(CursoSacramental)
class CursoSacramentalAdmin(admin.ModelAdmin):
    list_display        = ['id', 'feligres','sacramento', 'nombre_curso', 'fecha_inicio', 'fecha_fin', 'estado', 'responsable', 'created_at']
    list_filter         = []
    search_fields       = ['nombre_curso']
    prepopulated_fields = {}