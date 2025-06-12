from rest_framework import serializers
from proyectos.models.notificacion_modelo import Notificacion

class NotificacionSerializer(serializers.ModelSerializer):
    
    class Meta:
        moldel = Notificacion
        fields = '__all__'
        read_only_fields = ['fecha', 'leida']