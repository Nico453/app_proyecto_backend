from rest_framework.routers import DefaultRouter
from proyectos.views.proyecto_view import ProyectoViewSet
from proyectos.views.usuario_proyecto_view import UsuarioProyectoViewSet
from proyectos.views.invitacion_view import InvitacionViewSet
from proyectos.views.historias_view import HistoriaUsuarioViewSet

router = DefaultRouter()
router.register(r'proyecto', ProyectoViewSet, basename='proyecto')
router.register(r'usuario-proyectos', UsuarioProyectoViewSet, basename='usuario-proyecto')
router.register(r'invitacion', InvitacionViewSet, basename='invitacion')
router.register(r'historias', HistoriaUsuarioViewSet, basename='historias')

urlpatterns = router.urls
