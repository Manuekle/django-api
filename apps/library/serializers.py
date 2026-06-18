from rest_framework import serializers

from .models import Author, Book, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "bio"]


class BookSerializer(serializers.ModelSerializer):
    """Patrón habitual: leer anidado, escribir por id.

    - En la respuesta, `author` y `tags` se muestran completos (nested).
    - Al crear/editar se envía `author_id` y `tag_ids` (más simple para el cliente).
    """

    author = AuthorSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), source="author", write_only=True
    )
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        source="tags",
        many=True,
        write_only=True,
        required=False,
    )

    class Meta:
        model = Book
        fields = [
            "id", "title", "published_year", "cover",
            "author", "tags",            # solo lectura (nested)
            "author_id", "tag_ids",      # solo escritura
        ]


class AuthorDetailSerializer(AuthorSerializer):
    """Autor con sus libros anidados (lado inverso de la FK)."""

    books = BookSerializer(many=True, read_only=True)

    class Meta(AuthorSerializer.Meta):
        fields = AuthorSerializer.Meta.fields + ["books"]
