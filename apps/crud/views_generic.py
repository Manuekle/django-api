"""Estilo 2 — Vistas genéricas (generics).

DRF ya trae clases que resuelven los patrones comunes. Definís queryset y
serializer y obtenés list/create/retrieve/update/destroy gratis.
"""
from rest_framework import generics

from .models import Task
from .serializers import TaskSerializer


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
