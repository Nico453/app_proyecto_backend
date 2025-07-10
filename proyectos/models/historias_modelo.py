from django.db import models
from proyectos.models.usuario_proyecto_modelo import UsuarioProyecto

class HistoriaUsuario(models.Model):
    ESTADO_CHOICES = [
        ('Por Hacer', 'Por Hacer'),
        ('En Proceso', 'En Proceso'),
        ('Cerrada', 'Cerrada'),
    ]

    usuario_proyecto = models.ForeignKey(UsuarioProyecto, on_delete=models.CASCADE, related_name='historias_creadas')
    asignado_a = models.ForeignKey(UsuarioProyecto, on_delete=models.CASCADE, related_name='historias_asignadas', null=True, blank=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    puntos_historia = models.IntegerField()
    tiempo_estimado = models.IntegerField(help_text='Tiempo en horas')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Por Hacer')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo