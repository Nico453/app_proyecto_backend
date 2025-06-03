from rest_framework import serializers
from usuarios.models.rol_modelo import Rol
from rest_framework.validators import UniqueValidator

class RolSerializer(serializers.ModelSerializer):
    nombre_rol = serializers.CharField(
        max_length = 15, 
        validators = [
            UniqueValidator(
                queryset=Rol.objects.all(),
                message="Ya existe un rol con ese nombre"
            )
        ]
    )
    
    class Meta:
        model = Rol
        fields = '__all__'