"""Listado con paginación + filtros + búsqueda + ordenamiento.

Los backends de filtrado y la paginación están activados globalmente en
`REST_FRAMEWORK` (ver settings). Acá solo declaramos qué campos aplican.
"""
from rest_framework import generics

from .filters import ProductFilter
from .models import Product
from .serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # django-filter: filtros exactos / por rango (ver filters.py)
    filterset_class = ProductFilter
    # SearchFilter: ?search=texto  (busca en estos campos)
    search_fields = ["name"]
    # OrderingFilter: ?ordering=price  ó  ?ordering=-price
    ordering_fields = ["price", "stock", "created_at", "name"]
    ordering = ["-created_at"]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
