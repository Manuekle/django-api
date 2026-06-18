"""Rutas del ejemplo de relaciones (router con ViewSets).

- /api/library/authors/   (detalle incluye libros anidados)
- /api/library/books/     (lectura anidada, escritura por author_id/tag_ids)
- /api/library/tags/
"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet, BookViewSet, TagViewSet

router = DefaultRouter()
router.register(r"authors", AuthorViewSet)
router.register(r"books", BookViewSet)
router.register(r"tags", TagViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
