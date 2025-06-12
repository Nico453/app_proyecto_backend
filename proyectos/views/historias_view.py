from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from proyectos.models.historias_modelo import HistoriaUsuario
from proyectos.serializers.historias_serializer import HistoriaUsuarioSerializer

class HistoriaUsuarioViewSet(viewsets.ModelViewSet):
    queryset = HistoriaUsuario.objects.all()
    serializer_class = HistoriaUsuarioSerializer
    permission_classes = [IsAuthenticated]