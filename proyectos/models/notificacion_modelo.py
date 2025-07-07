from django.db import models
from django.conf import settings
from proyectos.models.invitacion_modelo import Invitacion
from proyectos.models.historias_modelo import HistoriaUsuario as Historia
from proyectos.models.tareas_modelo import Tarea

class Notificacion(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    mensaje = models.TextField()
    leida = models.BooleanField(default=False)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    
    
    # Relación opcional según el tipo
    invitacion = models.ForeignKey(Invitacion, null=True, blank=True, on_delete=models.SET_NULL)
    historia = models.ForeignKey(Historia, null=True, blank=True, on_delete=models.SET_NULL)
    tarea = models.ForeignKey(Tarea, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.titulo