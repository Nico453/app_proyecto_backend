from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from proyectos.models.notificacion_modelo import Notificacion
from proyectos.serializers.notificacion_serializer import NotificacionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


from drf_yasg.utils import swagger_auto_schema

class NotificacionViewSet(viewsets.ModelViewSet):
    serializer_class = NotificacionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Notificacion.objects.none()
        return Notificacion.objects.filter(usuario=self.request.user).order_by('-fecha_envio')
    
    @action(detail=True, methods=['post'])
    def marcar_leida(self, request, pk=None):
        notificacion = self.get_object()
        notificacion.leida = True
        notificacion.save()
        return Response({'mensaje': 'Notificación marcada como leída.'}, status=status.HTTP_200_OK)

    @swagger_auto_schema(tags=["proyectos_app.Notificacion"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Notificacion"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Notificacion"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Notificacion"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Notificacion"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Notificacion"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
