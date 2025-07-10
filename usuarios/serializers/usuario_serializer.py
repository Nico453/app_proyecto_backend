'''
    se trabajara los serializadores para:
    -registrar nuevo usuario
    -ver o actualizar usuario

'''

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from usuarios.models.usuario_modelo import Usuario
     
        
class RegistroSerializer(serializers.ModelSerializer):
    contrasena = serializers.CharField(
        write_only = True,
        min_length = 8,
        style = {"input_type": "password"}
    )
    correo = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=Usuario.objects.all(),
                message="Ya existe un usuario con este correo."
            )
        ]
    )
    class Meta:
        model = Usuario
        fields = ("id", "nombre", "correo", "contrasena",)
        extra_kwargs = {
            "correo": {"validators": [UniqueValidator(queryset=Usuario.objects.all())]}
        }
        
    def create(self, validated_data):
        password = validated_data.pop("contrasena")
        usuario = Usuario(**validated_data)
        usuario.set_password(password)
        usuario.save()
        return usuario
        
class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        read_only_fields = ("id", "correo", "fecha_creacion", "ultimo_acceso")
        