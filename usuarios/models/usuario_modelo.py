from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class UsuarioManager(BaseUserManager):
    def create_user(self, correo, password=None, **extra_fields):
        if not correo:
            raise ValueError("El correo es obligatorio")
        correo = self.normalize_email(correo)
        usuario = self.model(correo=correo, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("El superusuario debe tener is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("El superusuario debe tener is_superuser=True.")

        return self.create_user(correo, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    username        = None  # Eliminamos username
    nombre          = models.CharField(max_length=50)
    correo          = models.EmailField(unique=True)
    fecha_creacion  = models.DateTimeField(default=timezone.now)
    ultimo_acceso   = models.DateTimeField(auto_now=True)#no se actualiza el ultimo acceso 
    estado          = models.CharField(max_length=20, default="Activo")

    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD  = 'correo'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.correo
