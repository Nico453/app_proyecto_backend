from django.db import models



class Rol(models.Model):
    nombre_rol = models.CharField(max_length=15, unique=True)
    