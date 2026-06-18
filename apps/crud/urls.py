"""Rutas del ejemplo CRUD.

Los 3 estilos conviven bajo prefijos distintos para poder compararlos:

- /api/crud/tasks/            -> function-based views
- /api/crud/tasks-generic/    -> generics
- /api/crud/tasks-viewset/    -> ViewSet + router
"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views_function, views_generic
from .viewsets import TaskViewSet

router = DefaultRouter()
router.register(r"tasks-viewset", TaskViewSet, basename="task")

urlpatterns = [
    # Estilo 1: function-based
    path("tasks/", views_function.task_list, name="crud-fbv-list"),
    path("tasks/<int:pk>/", views_function.task_detail, name="crud-fbv-detail"),

    # Estilo 2: generics
    path("tasks-generic/", views_generic.TaskListCreate.as_view(), name="crud-generic-list"),
    path(
        "tasks-generic/<int:pk>/",
        views_generic.TaskRetrieveUpdateDestroy.as_view(),
        name="crud-generic-detail",
    ),

    # Estilo 3: viewset + router
    path("", include(router.urls)),
]
