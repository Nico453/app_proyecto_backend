from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from proyectos.models.invitacion_modelo import Invitacion
from proyectos.serializers.invitacion_serializer import InvitacionSerializer
from proyectos.models.usuario_proyecto_modelo import UsuarioProyecto
from proyectos.utils.notificacion_utils import enviar_correo_notificacion_invitacion
from proyectos.models.notificacion_modelo import Notificacion
from drf_yasg.utils import swagger_auto_schema


class InvitacionViewSet(viewsets.ModelViewSet):
    queryset = Invitacion.objects.all()
    serializer_class = InvitacionSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        
        invitacion = serializer.save()
        correo = invitacion.usuario.correo

        # Notificación interna
        Notificacion.objects.create(
            usuario=invitacion.usuario,
            titulo='Invitación a un proyecto',
            mensaje=f"Has sido invitado al proyecto '{invitacion.proyecto.nombre}' con rol'{invitacion.rol}'. Puedes aceptarla o rechazarla desde tu perfil.",
        )

        # Notificación por correo
        enviar_correo_notificacion_invitacion(correo, invitacion )
    
    
    
    
    @swagger_auto_schema(
    method='post',
    operation_summary="Aceptar invitacion",
    request_body=InvitacionSerializer,
    tags=["proyectos_app.Invitacion"]
    )
    @action(detail=True, methods=['post'])
    def aceptar(self, request, pk=None):
        invitacion = self.get_object()
        if invitacion.usuario != request.user:
            return Response({'error': 'No tienes permiso para responder esta invitación.'}, status=403)
        
        if invitacion.estado != 'Pendiente':
            return Response({'error': 'La invitación ya fue respondida.'}, status=400)

        # Validar que no esté ya asignado
        if UsuarioProyecto.objects.filter(usuario=invitacion.usuario, proyecto=invitacion.proyecto).exists():
            return Response({'error': 'Este usuario ya está en el proyecto.'}, status=400)
        
        if invitacion.rol.id == 2 and UsuarioProyecto.objects.filter(proyecto=invitacion.proyecto, rol__id=2).exists():
            return Response({'error': 'Este proyecto ya tiene un Scrum Master asignado.'}, status=400)

        UsuarioProyecto.objects.create(
            usuario=invitacion.usuario,
            proyecto=invitacion.proyecto,
            rol=invitacion.rol,
            estado='Activo'
        )

        invitacion.estado = 'Aceptada'
        invitacion.save()
        return Response({'mensaje': 'Invitación aceptada y usuario asignado al proyecto.'}, status=200)

    
    @swagger_auto_schema(
    method='post',
    operation_summary="Rechazar invitacion",
    request_body=InvitacionSerializer,
    tags=["proyectos_app.Invitacion"]
    )
    @action(detail=True, methods=['post'])
    def rechazar(self, request, pk=None):
        invitacion = self.get_object()
        if invitacion.usuario != request.user:
            return Response({'error': 'No tienes permiso para responder esta invitación.'}, status=403)
        
        if invitacion.estado != 'Pendiente':
            return Response({'error': 'La invitación ya fue respondida.'}, status=400)

        invitacion.estado = 'Rechazada'
        invitacion.save()
        return Response({'mensaje': 'Invitación rechazada.'}, status=200)
    
    
    @swagger_auto_schema(tags=["proyectos_app.Invitacion"],
                         operation_summary="Listar invitaciones",
                         operation_description="Retorna una lista con todos los usuarios invitados ya sean en estado Aceptada,Pendiente o Rechazada",
                         
                         )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Invitacion"],
                         operation_summary="Crea invitaciones",
                         operation_description="Crea una invitacion a un USUARIO de un PROYECTO con un ROL",
                         request_body=InvitacionSerializer,
                         )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Invitacion"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Invitacion"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Invitacion"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Invitacion"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)