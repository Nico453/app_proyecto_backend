from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from usuarios.models import Usuario

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    # obtener user y password
    correo = request.data.get('correo')
    contrasena = request.data.get('password')
    
    #valida que el user exista
    user = authenticate(correo = correo, password = contrasena)
    
    if user:
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                'refresh' : str(refresh),
                'token' : str(refresh.access_token)
            }
        )
    else:
        return Response(
            {
                'error' : 'Credenciales inavalidas'
            },
            status.HTTP_401_UNAUTHORIZED
        )
        
@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    nombre = request.data.get('nombre')
    correo = request.data.get('correo')
    password = request.data.get('password')
    
    if not nombre or not correo or not password:
        return Response({'error': 'Todos los campos son obligatorios.'}, status=status.HTTP_400_BAD_REQUEST)

    if Usuario.objects.filter(correo=correo).exists():
        return Response({'error': 'Ya existe un usuario con este correo.'}, status=status.HTTP_400_BAD_REQUEST)

    user = Usuario.objects.create_user(
        nombre=nombre,
        correo=correo,
        password=password
    )

    refresh = RefreshToken.for_user(user)

    return Response({
        'mensaje': 'Usuario registrado exitosamente.',
        'refresh': str(refresh),
        'token': str(refresh.access_token)
    }, status=status.HTTP_201_CREATED)