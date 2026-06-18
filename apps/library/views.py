from rest_framework import viewsets

from .models import Author, Book, Tag
from .serializers import (
    AuthorDetailSerializer,
    AuthorSerializer,
    BookSerializer,
    TagSerializer,
)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()

    def get_serializer_class(self):
        # En el detalle mostramos los libros anidados; en la lista, no.
        if self.action == "retrieve":
            return AuthorDetailSerializer
        return AuthorSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class BookViewSet(viewsets.ModelViewSet):
    # select_related/prefetch_related evitan el problema N+1 al serializar.
    queryset = Book.objects.select_related("author").prefetch_related("tags")
    serializer_class = BookSerializer
