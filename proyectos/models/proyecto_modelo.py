from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Proyecto(models.Model):
    ESTADO_CHOICES = [
        ('Activado', 'Activado'),
        ('Finalizado', 'Finalizado'),
    ]

    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Activado')
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proyectos')  

    def __str__(self):
        return self.nombre
