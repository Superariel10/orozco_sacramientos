from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from sacramentos.views.health   import health_check
from sacramentos.views.auth     import RegisterView, LogoutView
from sacramentos.views.padrinos import PadrinosViewSet
from sacramentos.views.registro_sacramento import RegistroSacramentoViewSet
from sacramentos.views.user     import UserViewSet
from sacramentos.views.sacramento import SacramentoViewSet
from sacramentos.serializers.auth import CustomTokenView
from sacramentos.views.feligres import FeligresViewSet
from sacramentos.views.curso_sacramental import CursoSacramentalViewSet


router = DefaultRouter()
router.register('users',      UserViewSet,      basename='user')
router.register('sacramentos', SacramentoViewSet,  basename='sacramento')
router.register('feligreses', FeligresViewSet,  basename='feligres')
router.register('registro_sacramento', RegistroSacramentoViewSet,  basename='registro_sacramento')
router.register('padrinos', PadrinosViewSet,  basename='padrinos')
router.register('curso_sacramental', CursoSacramentalViewSet, basename='curso_sacramental')

urlpatterns = [
    path('health/',             health_check),
    path('auth/register/',      RegisterView.as_view()),
    path('auth/login/',         CustomTokenView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/token/verify/',  TokenVerifyView.as_view()),
    path('auth/logout/',        LogoutView.as_view()),
    path('', include(router.urls)),
]