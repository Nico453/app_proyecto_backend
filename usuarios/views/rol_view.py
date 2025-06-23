from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from usuarios.models.rol_modelo import Rol
from usuarios.serializers.rol_serializer import RolSerializer
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method='get',
    operation_summary="Listar todos los roles",
    tags=["usuarios_app.Roles"]
)
@api_view(['GET'])
def list_rol(request):
    ''' Listar roles '''
    list_rol = Rol.objects.all()
    serializer = RolSerializer(list_rol, many = True)
    return Response(serializer.data, status.HTTP_200_OK)



@swagger_auto_schema(
    method='post',
    operation_summary="Crear un nuevo rol",
    request_body=RolSerializer,
    tags=["usuarios_app.Roles"]
)
@api_view(['POST'])
@permission_classes([AllowAny])
def create_rol(request):
    ''' Listar roles '''
    serializer = RolSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    
    
    
@swagger_auto_schema(
    method='get',
    operation_summary="Obtener detalle de un rol",
    tags=["usuarios_app.Roles"]
)
@swagger_auto_schema(
    method='put',
    operation_summary="Actualizar un rol",
    request_body=RolSerializer,
    tags=["usuarios_app.Roles"]
)
@swagger_auto_schema(
    method='delete',
    operation_summary="Eliminar un rol",
    tags=["usuarios_app.Roles"]
)
@api_view(['GET', 'PUT', 'DELETE'])
def detail_rol(request, rol_id):
    rol = get_object_or_404(Rol, id = rol_id)
    
    if request.method == 'GET':
        serializer = RolSerializer(rol)
        return Response(serializer.data, status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = RolSerializer(Rol, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    if request.method == 'DELETE':
        rol.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    
    @swagger_auto_schema(tags=["usuarios_app.Rol"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["usuarios_app.Rol"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["usuarios_app.Rol"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["usuarios_app.Rol"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["usuarios_app.Rol"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["usuarios_app.Rol"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)