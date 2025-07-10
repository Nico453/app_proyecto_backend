from rest_framework import serializers
from proyectos.models.usuario_proyecto_modelo import UsuarioProyecto
from proyectos.serializers.proyecto_serializer import ProyectoSerializer

class UsuarioProyectoSerializer(serializers.ModelSerializer):
    proyecto = ProyectoSerializer()
    class Meta:
        model = UsuarioProyecto
        fields = '__all__'
        
    def validate(self, data):
        usuario = data.get('usuario')
        proyecto = data.get('proyecto')
        rol = data.get('rol')

        if UsuarioProyecto.objects.filter(usuario=usuario, proyecto=proyecto).exists():
            raise serializers.ValidationError("Este usuario ya está asignado a este proyecto.")
        
        
        if rol.id == 2 and UsuarioProyecto.objects.filter(proyecto=proyecto, rol__id=2).exists():
            raise serializers.ValidationError("Ya existe un Scrum Master en este proyecto.")
        
        

        return data