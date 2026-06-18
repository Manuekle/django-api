from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("tech", "Tecnología"),
        ("home", "Hogar"),
        ("books", "Libros"),
        ("toys", "Juguetes"),
    ]

    name = models.CharField("nombre", max_length=200)
    category = models.CharField(
        "categoría", max_length=20, choices=CATEGORY_CHOICES, default="tech"
    )
    price = models.DecimalField("precio", max_digits=9, decimal_places=2)
    stock = models.PositiveIntegerField("stock", default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
