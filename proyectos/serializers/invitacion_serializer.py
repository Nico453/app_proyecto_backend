from rest_framework import serializers
from proyectos.models.invitacion_modelo import Invitacion

class InvitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitacion
        fields = '__all__'