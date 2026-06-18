from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "done", "created_at"]
    list_filter = ["done"]
    list_editable = ["done"]
    search_fields = ["title"]
