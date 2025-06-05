from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from proyectos.models.proyecto_modelo import Proyecto
from proyectos.serializers.proyecto_serializer import ProyectoSerializer
from proyectos.models.usuario_proyecto_modelo import UsuarioProyecto
from usuarios.models.rol_modelo import Rol

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        proyecto = serializer.save()
        usuario = self.request.user

        
        rol_pm = Rol.objects.get(id=1) 

        UsuarioProyecto.objects.create(
            usuario=usuario,
            proyecto=proyecto,
            rol=rol_pm,
            estado="Activo"
        )