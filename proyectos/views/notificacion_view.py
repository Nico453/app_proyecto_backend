from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from proyectos.models.notificacion_modelo import Notificacion
from proyectos.serializers.notificacion_serializer import NotificacionSerializer

class NotificacionViewSet(viewsets.ModelViewSet):
    
    serializer_class = NotificacionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Notificacion.objects.filter(usuario=self.request.user).order_by('-fecha')