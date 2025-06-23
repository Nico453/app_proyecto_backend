from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from usuarios.models import Usuario
from usuarios.serializers.usuario_serializer import RegistroSerializer
from drf_yasg.utils import swagger_auto_schema

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
    
    @swagger_auto_schema(tags=["usuarios_app.Usuarios"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["usuarios_app.Usuarios"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["usuarios_app.Usuarios"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["usuarios_app.Usuarios"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["usuarios_app.Usuarios"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["usuarios_app.Usuarios"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)