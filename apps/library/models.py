from django.db import models


class Author(models.Model):
    name = models.CharField("nombre", max_length=200)
    bio = models.TextField("biografía", blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField("nombre", max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField("título", max_length=200)
    # Relación uno-a-muchos: un autor tiene muchos libros.
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books"
    )
    # Relación muchos-a-muchos: un libro tiene varias etiquetas.
    tags = models.ManyToManyField(Tag, related_name="books", blank=True)
    cover = models.ImageField("portada", upload_to="covers/", null=True, blank=True)
    published_year = models.PositiveIntegerField("año", null=True, blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
