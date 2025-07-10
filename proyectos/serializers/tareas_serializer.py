from rest_framework import serializers
from proyectos.models.tareas_modelo import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'