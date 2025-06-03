from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

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