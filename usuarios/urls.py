from django.urls import path, include
from usuarios.views.rol_view import list_rol, create_rol, detail_rol

# importar viewset de usuarios
from rest_framework.routers import DefaultRouter
from usuarios.views.usuario_view import UsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls)),
    path('rol/', list_rol, name='lista_roles'),
    path('rol/create/', create_rol, name='crear_rol'),
    path('rol/<int:rol_id>/', detail_rol, name='detalles_rol'),
]



