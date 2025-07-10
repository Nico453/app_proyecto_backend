from rest_framework import serializers
from proyectos.models.invitacion_modelo import Invitacion
from proyectos.models.usuario_proyecto_modelo import UsuarioProyecto

class InvitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitacion
        fields = '__all__'
        
    def validate(self, data):
        usuario = data.get('usuario')
        proyecto = data.get('proyecto')
        rol = data.get('rol')

        
        if rol.id == 1:
            raise serializers.ValidationError("No puedes invitar usuarios con el rol PMO.")
        
        if rol.id == 2:
            ya_asignado = UsuarioProyecto.objects.filter(proyecto=proyecto, rol__id=2).exists()
            ya_invitado = Invitacion.objects.filter(proyecto=proyecto, rol__id=2, estado='Pendiente').exists()

            if ya_asignado or ya_invitado:
                raise serializers.ValidationError("Este proyecto ya tiene un Scrum Master asignado o invitado.")

        
        if UsuarioProyecto.objects.filter(usuario=usuario, proyecto=proyecto).exists():
            raise serializers.ValidationError("Este usuario ya está asignado a este proyecto.")

        
        if Invitacion.objects.filter(usuario=usuario, proyecto=proyecto, estado='Pendiente').exists():
            raise serializers.ValidationError("Este usuario ya tiene una invitación pendiente para este proyecto.")

        
        return data