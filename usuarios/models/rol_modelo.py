from django.db import models



class Rol(models.Model):
    nombre_rol = models.CharField(max_length=15, unique=True)
    
    def __str__(self):
        return self.nombre_rol