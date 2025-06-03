from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from usuarios.models import Usuario
from django.forms import TextInput, Textarea
from django import forms

class UsuarioAdmin(BaseUserAdmin):
    model = Usuario
    list_display = ('correo', 'nombre', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('correo', 'nombre')
    ordering = ('correo',)

    fieldsets = (
        (None, {'fields': ('correo', 'nombre', 'password')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas', {'fields': ('fecha_creacion', 'ultimo_acceso')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('correo', 'nombre', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

admin.site.register(Usuario, UsuarioAdmin)
