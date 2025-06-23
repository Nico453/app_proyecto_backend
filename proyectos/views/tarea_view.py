from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from proyectos.models.tareas_modelo import Tarea
from proyectos.serializers.tareas_serializer import TareaSerializer
from drf_yasg.utils import swagger_auto_schema

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [IsAuthenticated]
    
    
    
    
    @swagger_auto_schema(tags=["proyectos_app.Tarea"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Tarea"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Tarea"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Tarea"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Tarea"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["proyectos_app.Tarea"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs) 