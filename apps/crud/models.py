from django.db import models


class Task(models.Model):
    """Tarea simple, sin relaciones, para enfocarse solo en el CRUD."""

    title = models.CharField("título", max_length=200)
    done = models.BooleanField("completada", default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
