"""Vistas de UI: renderizan templates Django que consumen las APIs vía fetch.

Son intencionalmente simples (sin lógica de negocio) para que el foco quede en
las APIs. Cada template demuestra cómo un cliente consume el ejemplo asociado.
"""
from django.shortcuts import render

EXAMPLES = [
    {
        "slug": "crud",
        "title": "CRUD completo",
        "desc": "Crear, leer, actualizar y borrar el mismo modelo en 3 estilos: "
                "function-based, generics y ViewSet.",
        "api": "/api/crud/",
        "ui": "/ui/crud/",
    },
    {
        "slug": "auth",
        "title": "Autenticación JWT",
        "desc": "Registro, login (obtener token), refresh y un endpoint "
                "protegido que devuelve el usuario actual.",
        "api": "/api/auth/",
        "ui": "/ui/auth/",
    },
    {
        "slug": "catalog",
        "title": "Paginación, filtros y búsqueda",
        "desc": "Listado de productos con paginación, django-filter, búsqueda "
                "por texto y ordenamiento.",
        "api": "/api/catalog/products/",
        "ui": "/ui/catalog/",
    },
    {
        "slug": "library",
        "title": "Relaciones y nested serializers",
        "desc": "Autores, libros (FK) y etiquetas (M2M) con serializers "
                "anidados y subida de imagen de portada.",
        "api": "/api/library/",
        "ui": "/ui/library/",
    },
]


def index(request):
    return render(request, "index.html", {"examples": EXAMPLES})


def crud(request):
    return render(request, "examples/crud.html")


def auth(request):
    return render(request, "examples/auth.html")


def catalog(request):
    return render(request, "examples/catalog.html")


def library(request):
    return render(request, "examples/library.html")
