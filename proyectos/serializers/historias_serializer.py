from rest_framework import serializers
from proyectos.models.historias_modelo import HistoriaUsuario
from proyectos.serializers.usuario_proyecto_serializer import UsuarioProyectoSerializer

class HistoriaUsuarioSerializer(serializers.ModelSerializer):
    asignado_a = UsuarioProyectoSerializer()
    class Meta:
        model = HistoriaUsuario
        fields = '__all__'

    def validate(self, data):
        request = self.context.get('request')
        if not request:
            raise serializers.ValidationError("No se pudo verificar el usuario autenticado.")

        usuario = request.user
        usuario_proyecto = data.get('usuario_proyecto')

           
        usuario_proyecto = data.get('usuario_proyecto') or getattr(self.instance, 'usuario_proyecto', None)
        if not usuario_proyecto:
            raise serializers.ValidationError("No se encontró relación usuario-proyecto.")

       
        if request.method == 'POST' or 'estado' in data:
            if usuario_proyecto.usuario != usuario:
                raise serializers.ValidationError("Solo puedes modificar tus propias historias.")
            if usuario_proyecto.rol.id != 2:  
                raise serializers.ValidationError("Solo el Scrum Master puede realizar esta acción.")

        return data
    