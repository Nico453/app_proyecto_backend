from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from usuarios.models import Usuario
from usuarios.serializers.usuario_serializer import RegistroSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = RegistroSerializer
    permission_classes = [AllowAny]
    '''
     def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]   
    '''
