from rest_framework import serializers
from proyectos.models.historias_modelo import HistoriaUsuario

class HistoriaUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaUsuario
        fields = '__all__'

    def validate(self, data):
        request = self.context.get('request')
        if not request:
            raise serializers.ValidationError("No se pudo verificar el usuario autenticado.")

        usuario = request.user
        usuario_proyecto = data.get('usuario_proyecto')

        if usuario_proyecto.usuario != usuario:
            raise serializers.ValidationError("Solo puedes crear historias desde tus proyectos.")

        if usuario_proyecto.rol_id != 2:
            raise serializers.ValidationError("Solo los usuarios con rol Scrum Master pueden crear historias.")

        return data