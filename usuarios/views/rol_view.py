from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from usuarios.models.rol_modelo import Rol
from usuarios.serializers.rol_serializer import RolSerializer

@api_view(['GET'])
def list_rol(request):
    ''' Listar roles '''
    list_rol = Rol.objects.all()
    serializer = RolSerializer(list_rol, many = True)
    return Response(serializer.data, status.HTTP_200_OK)

@api_view(['POST'])
def create_rol(request):
    ''' Listar roles '''
    serializer = RolSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
    
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