from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from proyectos.models.historias_modelo import HistoriaUsuario
from proyectos.serializers.historias_serializer import HistoriaUsuarioSerializer
from proyectos.utils.notificacion_utils import enviar_correo_notificacion_historia_usuario
from proyectos.models.notificacion_modelo import Notificacion
from drf_yasg.utils import swagger_auto_schema





class HistoriaUsuarioViewSet(viewsets.ModelViewSet):
    queryset = HistoriaUsuario.objects.all()
    serializer_class = HistoriaUsuarioSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        
        historia = serializer.save()
        usuario_destino = historia.asignado_a.usuario
        correo =  usuario_destino.correo
        proyecto_nombre = historia.usuario_proyecto.proyecto.nombre

        # Notificación interna
        Notificacion.objects.create(
            usuario=usuario_destino,
            titulo='Historia nueva asignada',
            mensaje=f"Se te ha asignado la historia: '{historia.titulo}' en el proyecto '{proyecto_nombre}'."
        )
        # Notificación por correo
        enviar_correo_notificacion_historia_usuario(correo, historia )
        
        
        
    @swagger_auto_schema(tags=["proyectos_app.HU"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.HU"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.HU"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.HU"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.HU"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.HU"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)