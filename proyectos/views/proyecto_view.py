from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from proyectos.models.proyecto_modelo import Proyecto
from proyectos.serializers.proyecto_serializer import ProyectoSerializer
from proyectos.models.usuario_proyecto_modelo import UsuarioProyecto
from usuarios.models.rol_modelo import Rol
from proyectos.serializers.usuario_proyecto_serializer import UsuarioProyectoSerializer

from drf_yasg.utils import swagger_auto_schema


class ProyectoViewSet(viewsets.ModelViewSet):
    """
    CRUD de Proyectos filtrado por usuario + asignación automática de rol PM al crear.
    """
    serializer_class = ProyectoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Durante la generación de docs o si no hay usuario autenticado,
        # devolvemos un QuerySet vacío para evitar el TypeError.
        if getattr(self, 'swagger_fake_view', False) or self.request.user.is_anonymous:
            return Proyecto.objects.none()

        usuario = self.request.user
        proyectos_ids = UsuarioProyecto.objects.filter(
            usuario=usuario
        ).values_list('proyecto_id', flat=True)
        return Proyecto.objects.filter(id__in=proyectos_ids)

    def perform_create(self, serializer):
        proyecto = serializer.save(usuario=self.request.user)

        # Asignar el rol PM al creador
        rol_pm = Rol.objects.get(id=1)
        UsuarioProyecto.objects.create(
            usuario=self.request.user,
            proyecto=proyecto,
            rol=rol_pm,
            estado="Activo"
        )

    @swagger_auto_schema(tags=["proyectos_app.Proyecto"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Proyecto"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Proyecto"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Proyecto"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Proyecto"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Proyecto"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
