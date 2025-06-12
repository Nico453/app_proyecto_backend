from proyectos.models.notificacion_modelo import Notificacion
from django.core.mail import send_mail
from django.conf import settings

def crear_notificacion(usuario, titulo, mensaje):
    Notificacion.objects.create(usuario=usuario, titulo=titulo, mensaje=mensaje)

    send_mail(
        subject=titulo,
        message=mensaje,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[usuario.email],
        fail_silently=False,
    )
    
    
    
def enviar_correo_bienvenida(correo_destino, nombre_usuario):
    asunto = '¡Bienvenido a la plataforma!'
    mensaje = f'Hola {nombre_usuario}, tu cuenta ha sido creada exitosamente.'
    send_mail(
        subject=asunto,
        message=mensaje,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[correo_destino],
        fail_silently=False
    )
    
def enviar_correo_ya_registrado(correo_destino):
    asunto = 'Intento de registro con correo existente'
    mensaje = (
        f'Hola,\n\nRecibimos un intento de registro con este correo, pero ya está asociado a una cuenta existente. '
        'Si no fuiste tú, puedes ignorar este mensaje. Si olvidaste tu contraseña, intenta recuperarla desde la plataforma.'
    )
    send_mail(
        subject=asunto,
        message=mensaje,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[correo_destino],
        fail_silently=False
    )
    
def enviar_correo_notificacion_invitacion(correo_destino, invitacion):
    asunto='Has recibido una invitación'
    mensaje = f"Has sido invitado al proyecto '{invitacion.proyecto.nombre}'.\n\nIngresa al sistema para aceptarla o rechazarla desde tu perfil."
    
    send_mail(
        subject=asunto,
        message=mensaje,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[correo_destino],
        fail_silently=False
    )
