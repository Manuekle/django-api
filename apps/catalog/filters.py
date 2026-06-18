"""Filtros declarativos con django-filter.

Permiten consultas como:
    /api/catalog/products/?category=tech&min_price=100&max_price=500
"""
import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):
    # Rango de precio: ?min_price=100&max_price=500
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    # Solo productos con stock: ?in_stock=true
    in_stock = django_filters.BooleanFilter(method="filter_in_stock")

    class Meta:
        model = Product
        fields = ["category", "min_price", "max_price", "in_stock"]

    def filter_in_stock(self, queryset, name, value):
        if value:
            return queryset.filter(stock__gt=0)
        return queryset
