"""Rutas del ejemplo de paginación/filtros/búsqueda.

- GET /api/catalog/products/?page=2
- GET /api/catalog/products/?category=tech&min_price=100&max_price=500
- GET /api/catalog/products/?search=teclado
- GET /api/catalog/products/?ordering=-price
"""
from django.urls import path

from .views import ProductDetail, ProductList

urlpatterns = [
    path("products/", ProductList.as_view(), name="catalog-list"),
    path("products/<int:pk>/", ProductDetail.as_view(), name="catalog-detail"),
]
