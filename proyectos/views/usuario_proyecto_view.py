from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from proyectos.models.usuario_proyecto_modelo import UsuarioProyecto
from proyectos.serializers.usuario_proyecto_serializer import UsuarioProyectoSerializer

class UsuarioProyectoViewSet(viewsets.ModelViewSet):
    queryset = UsuarioProyecto.objects.all()
    serializer_class = UsuarioProyectoSerializer
    permission_classes = [IsAuthenticated]