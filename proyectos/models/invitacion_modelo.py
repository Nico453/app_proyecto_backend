from django.db import models
from django.conf import settings
from proyectos.models.proyecto_modelo import Proyecto
from usuarios.models.rol_modelo import Rol

class Invitacion(models.Model):
    ESTADO_CHOICES = [
        ('Aceptada', 'Aceptada'),
        ('Pendiente', 'Pendiente'),
        ('Rechazada', 'Rechazada'),
    ]
    
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL,null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')
    fecha_envio = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.usuario