# Ejemplo 3 — Paginación, filtros y búsqueda

Demuestra cómo refinar un listado grande con las tres herramientas que vienen
con DRF + `django-filter`: **paginación**, **filtros**, **búsqueda** y
**ordenamiento**. Todas se combinan en la misma URL.

## Endpoint

```
GET /api/catalog/products/
```

| Capacidad | Query param | Ejemplo |
|---|---|---|
| Paginación | `page` | `?page=2` |
| Filtro exacto | `category` | `?category=tech` |
| Filtro por rango | `min_price` / `max_price` | `?min_price=100&max_price=500` |
| Filtro custom | `in_stock` | `?in_stock=true` |
| Búsqueda de texto | `search` | `?search=teclado` |
| Ordenamiento | `ordering` | `?ordering=-price` |

Se pueden combinar: `?category=tech&min_price=100&ordering=price&page=2`.

## Respuesta paginada

```json
{
  "count": 42,
  "next": "http://.../products/?page=3",
  "previous": "http://.../products/?page=1",
  "results": [ ... ]
}
```

## Conceptos clave

- La paginación (`PageNumberPagination`, `PAGE_SIZE=5`) y los `DEFAULT_FILTER_BACKENDS`
  están activados **globalmente** en `settings.py`; la vista solo declara qué
  campos aplican.
- `filterset_class` (django-filter) define filtros exactos, por rango y custom
  (ver `filters.py`).
- `search_fields` habilita `?search=`; `ordering_fields` habilita `?ordering=`.
