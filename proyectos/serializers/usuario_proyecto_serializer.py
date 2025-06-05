from rest_framework import serializers
from proyectos.models.usuario_proyecto_modelo import UsuarioProyecto

class UsuarioProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioProyecto
        fields = '__all__'
        
    def validate(self, data):
        usuario = data.get('usuario')
        proyecto = data.get('proyecto')

        if UsuarioProyecto.objects.filter(usuario=usuario, proyecto=proyecto).exists():
            raise serializers.ValidationError("Este usuario ya está asignado a este proyecto.")

        return data