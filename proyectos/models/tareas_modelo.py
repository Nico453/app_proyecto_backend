from django.db import models
from proyectos.models.historias_modelo import HistoriaUsuario
from proyectos.models.usuario_proyecto_modelo import UsuarioProyecto

class Tarea(models.Model):
    ESTADO_CHOICES = [
        ('Por Hacer', 'Por Hacer'),
        ('En Progreso', 'En Progreso'),
        ('Hecha', 'Hecha'),
    ]
    
    historia_usuario = models.ForeignKey(HistoriaUsuario, on_delete=models.CASCADE)
    desarrollador = models.ForeignKey(UsuarioProyecto, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Por Hacer')
    archivos = models.FileField(upload_to='tareas_archivo/', null=True, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.titulo