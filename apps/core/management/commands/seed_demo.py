"""Carga datos de ejemplo para que las demos de UI muestren contenido.

Uso:
    python manage.py seed_demo
    python manage.py seed_demo --fresh   # borra los datos de ejemplo antes
"""
from decimal import Decimal

from django.core.management.base import BaseCommand

from apps.catalog.models import Product
from apps.crud.models import Task
from apps.library.models import Author, Book, Tag


class Command(BaseCommand):
    help = "Carga datos de ejemplo para las demos."

    def add_arguments(self, parser):
        parser.add_argument(
            "--fresh", action="store_true",
            help="Borra los datos de ejemplo antes de cargar.",
        )

    def handle(self, *args, **options):
        if options["fresh"]:
            Task.objects.all().delete()
            Product.objects.all().delete()
            Book.objects.all().delete()
            Author.objects.all().delete()
            Tag.objects.all().delete()
            self.stdout.write("Datos previos borrados.")

        self._seed_tasks()
        self._seed_products()
        self._seed_library()
        self.stdout.write(self.style.SUCCESS("Datos de ejemplo cargados."))

    def _seed_tasks(self):
        if Task.objects.exists():
            return
        for title, done in [
            ("Aprender serializers", True),
            ("Entender los ViewSets", False),
            ("Practicar paginación", False),
        ]:
            Task.objects.create(title=title, done=done)

    def _seed_products(self):
        if Product.objects.exists():
            return
        data = [
            ("Teclado mecánico", "tech", "75.00", 12),
            ("Mouse inalámbrico", "tech", "30.00", 0),
            ("Lámpara de escritorio", "home", "45.50", 8),
            ("Set de sábanas", "home", "60.00", 5),
            ("Clean Code", "books", "32.00", 20),
            ("Cubo Rubik", "toys", "15.00", 40),
            ("Monitor 27\"", "tech", "210.00", 3),
            ("Cafetera", "home", "89.90", 7),
        ]
        for name, cat, price, stock in data:
            Product.objects.create(
                name=name, category=cat, price=Decimal(price), stock=stock
            )

    def _seed_library(self):
        if Book.objects.exists():
            return
        ficcion, _ = Tag.objects.get_or_create(name="ficción")
        clasico, _ = Tag.objects.get_or_create(name="clásico")
        tecnico, _ = Tag.objects.get_or_create(name="técnico")

        cortazar = Author.objects.create(name="Julio Cortázar")
        martin = Author.objects.create(name="Robert C. Martin")

        rayuela = Book.objects.create(
            title="Rayuela", author=cortazar, published_year=1963
        )
        rayuela.tags.set([ficcion, clasico])

        clean = Book.objects.create(
            title="Clean Code", author=martin, published_year=2008
        )
        clean.tags.set([tecnico])
