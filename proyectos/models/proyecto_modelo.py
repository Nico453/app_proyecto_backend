from django.db import models

class Proyecto(models.Model):
    ESTADO_CHOICES = [
        ('Activado', 'Activado'),
          ('Finalizado', 'Finalizado'),
    ]
    
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Activado')
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre