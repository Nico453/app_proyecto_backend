from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from proyectos.models.usuario_proyecto_modelo import UsuarioProyecto
from proyectos.serializers.usuario_proyecto_serializer import UsuarioProyectoSerializer
from drf_yasg.utils import swagger_auto_schema

class UsuarioProyectoViewSet(viewsets.ModelViewSet):
    queryset = UsuarioProyecto.objects.all()
    serializer_class = UsuarioProyectoSerializer
    permission_classes = [IsAuthenticated]
    
    
    @swagger_auto_schema(tags=["proyectos_app.UsuarioProyecto"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.UsuarioProyecto"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.UsuarioProyecto"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.UsuarioProyecto"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.UsuarioProyecto"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.UsuarioProyecto"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs) 