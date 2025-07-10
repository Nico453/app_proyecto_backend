from rest_framework import serializers
from proyectos.models.proyecto_modelo import Proyecto

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ['id', 'nombre', 'estado', 'fecha_actualizacion']  # usuario excluido
        read_only_fields = ['fecha_actualizacion']
