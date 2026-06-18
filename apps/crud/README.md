# Ejemplo 1 — CRUD completo

Demuestra las **operaciones CRUD** (Create, Read, Update, Delete) sobre un
modelo simple (`Task`) en **tres estilos** distintos de DRF, para que compares
cuándo conviene cada uno.

| Estilo | Archivo | Ruta base | Cuándo usarlo |
|---|---|---|---|
| Function-based | `views_function.py` | `/api/crud/tasks/` | Para entender qué pasa por dentro; control total. |
| Generics | `views_generic.py` | `/api/crud/tasks-generic/` | Patrones comunes con poco código. |
| ViewSet + Router | `viewsets.py` | `/api/crud/tasks-viewset/` | Lo más usado en proyectos reales. |

Los tres consumen el **mismo** `models.py` y `serializers.py`.

## Endpoints

```
GET    /api/crud/tasks/              lista
POST   /api/crud/tasks/              crea            {"title": "..."}
GET    /api/crud/tasks/<id>/         detalle
PUT    /api/crud/tasks/<id>/         reemplaza
PATCH  /api/crud/tasks/<id>/         actualiza parcial
DELETE /api/crud/tasks/<id>/         borra
```

(idéntico para `tasks-generic/` y `tasks-viewset/`)

## Probar con curl

```bash
curl -X POST http://127.0.0.1:8000/api/crud/tasks/ -d "title=Aprender DRF"
curl http://127.0.0.1:8000/api/crud/tasks/
curl -X PATCH http://127.0.0.1:8000/api/crud/tasks/1/ \
     -H "Content-Type: application/json" -d '{"done": true}'
curl -X DELETE http://127.0.0.1:8000/api/crud/tasks/1/
```

## Conceptos clave

- `@api_view` decora funciones y les da el `request`/`Response` de DRF.
- `get_object_or_404` devuelve 404 si el objeto no existe.
- `generics.ListCreateAPIView` y `RetrieveUpdateDestroyAPIView` cubren el CRUD.
- `ModelViewSet` + `DefaultRouter` generan todas las rutas automáticamente.
