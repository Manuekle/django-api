# Ejemplo 4 — Relaciones y nested serializers

Demuestra cómo modelar y serializar **relaciones** entre modelos y cómo subir
una **imagen**. Hay tres modelos:

- `Author` 1—N `Book`  (ForeignKey)
- `Book` N—M `Tag`     (ManyToMany)
- `Book.cover`         (ImageField, subida de archivo)

## Endpoints (router)

```
GET/POST          /api/library/authors/
GET/PUT/DELETE    /api/library/authors/<id>/    (detalle incluye libros anidados)
GET/POST          /api/library/books/
GET/PUT/DELETE    /api/library/books/<id>/
GET/POST          /api/library/tags/
```

## Crear un libro con relaciones

Se **lee** anidado pero se **escribe** por id:

```bash
curl -X POST http://127.0.0.1:8000/api/library/books/ \
     -H "Content-Type: application/json" \
     -d '{"title":"Rayuela","author_id":1,"tag_ids":[1,2],"published_year":1963}'
```

Respuesta (anidada):

```json
{
  "id": 1,
  "title": "Rayuela",
  "author": {"id": 1, "name": "Cortázar", "bio": ""},
  "tags": [{"id": 1, "name": "ficción"}],
  "cover": null
}
```

## Subir la portada (multipart)

```bash
curl -X PATCH http://127.0.0.1:8000/api/library/books/1/ \
     -F "cover=@/ruta/a/portada.jpg"
```

## Conceptos clave

- **Leer anidado / escribir por id**: `AuthorSerializer(read_only=True)` para la
  respuesta y `PrimaryKeyRelatedField(..., source="author", write_only=True)`
  para la entrada. Patrón muy común y cómodo para el cliente.
- El **lado inverso** de la FK (`related_name="books"`) permite anidar los libros
  del autor en su detalle.
- `select_related` / `prefetch_related` evitan el problema **N+1** de consultas.
- `ImageField` + envío `multipart/form-data` para subir archivos.
