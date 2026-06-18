"""Estilo 3 — ViewSet + Router.

El más compacto: una sola clase cubre todo el CRUD y el router arma las URLs
automáticamente. Es lo que se usa en la mayoría de proyectos reales.
"""
from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
