from django.db import models
from django.conf import settings
from proyectos.models.proyecto_modelo import Proyecto
from usuarios.models.rol_modelo import Rol


class UsuarioProyecto(models.Model):
    ESTADO_CHOICES = [
        ('Activo','Activo'),
        ('Inactivo','Inactivo'),
        ('Eliminado','Eliminado')
    ]
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Activo')
    fecha_asignado = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.usuario} en {self.proyecto} como {self.rol}"