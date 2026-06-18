# Django API Learning Playground — Diseño

Fecha: 2026-06-17

## Objetivo

Convertir este repo (hoy: una sola app `base` con un endpoint de solo lectura y
un README copiado de DRF) en un **laboratorio de práctica** para aprender a
construir APIs con Django REST Framework. Cada concepto vive en su propia app
Django, aislado y documentado, más plantillas de UABI (Django templates) que
consumen las APIs. Todo separado y organizado.

## Audiencia

Personas aprendiendo a hacer APIs con Django. Documentación en español, nombres
de módulo en inglés (convención Django/Python).

## Decisiones (confirmadas con el usuario)

1. **Una app Django por ejemplo**, bajo `apps/`.
2. **4 ejemplos**: CRUD completo, Auth JWT, Paginación+filtros+búsqueda,
   Relaciones+nested serializers (incluye upload de imagen).
3. **UI**: templates Django simples (HTML+CSS, sin build). Se borra el build
   React compilado viejo (`staticfiles/js/*.chunk.js`, `frontend/index.html`).
4. **Limpieza completa**: `requirements.txt` mínimo, secrets vía `.env`
   (python-dotenv), README propio, **SQLite por defecto** para arranque fácil.

## Estructura objetivo

```
django-api/
├── manage.py
├── requirements.txt            # mínimo: Django 4.2 LTS, DRF, simplejwt, django-filter, Pillow, dotenv, cors
├── .env.example                # SECRET_KEY, DEBUG, DB opcional
├── .gitignore                  # venv, *.sqlite3, __pycache__, .env, staticfiles
├── README.md                   # propio: qué es, cómo correr, índice de ejemplos
├── backend/
│   ├── settings.py             # SQLite default, secrets desde .env, apps registradas
│   ├── urls.py                 # landing + /api/<ejemplo>/...
│   └── ...
├── apps/
│   ├── __init__.py
│   ├── crud/                   # Ej 1 — CRUD del modelo Task en 3 estilos
│   │   ├── models.py           # Task
│   │   ├── serializers.py
│   │   ├── views_function.py   # FBV con @api_view
│   │   ├── views_generic.py    # generics.ListCreate / RetrieveUpdateDestroy
│   │   ├── viewsets.py         # ModelViewSet + router
│   │   ├── urls.py             # monta los 3 estilos bajo sub-rutas
│   │   ├── admin.py, tests.py, migrations/
│   │   └── README.md           # explica el ejemplo
│   ├── auth_jwt/               # Ej 2 — registro, login, refresh, perfil protegido
│   │   ├── serializers.py      # RegisterSerializer, UserSerializer
│   │   ├── views.py            # register, me (protegido)
│   │   ├── urls.py             # /register /login /refresh /me
│   │   └── README.md, tests.py
│   ├── catalog/               # Ej 3 — paginación + django-filter + search + ordering
│   │   ├── models.py           # Product (category, price, stock, created)
│   │   ├── serializers.py
│   │   ├── filters.py          # ProductFilter (django-filter)
│   │   ├── views.py            # ListAPIView con pagination/filter/search/order
│   │   ├── urls.py
│   │   └── README.md, tests.py, migrations/
│   └── library/               # Ej 4 — relaciones FK/M2M + nested + upload imagen
│       ├── models.py           # Author, Book(FK author, cover image), Tag(M2M)
│       ├── serializers.py      # nested read + writable
│       ├── views.py            # ViewSets
│       ├── urls.py
│       └── README.md, tests.py, migrations/
├── templates/                  # UI server-rendered
│   ├── base.html               # layout + estilos compartidos
│   ├── index.html              # landing: tarjetas por ejemplo, links a browsable API + demo
│   └── examples/
│       ├── crud.html           # fetch + render lista Task, crear/borrar
│       ├── auth.html           # form login -> guarda JWT -> llama /me
│       ├── catalog.html        # buscador + filtros + paginación
│       └── library.html        # lista libros con autor y tags
├── static/
│   └── css/styles.css
└── docs/superpowers/specs/...
```

## Rutas API

| Ejemplo | Prefijo | Endpoints clave |
|---|---|---|
| crud | `/api/crud/` | `tasks/` (FBV), `tasks-generic/`, `tasks-viewset/` (router) |
| auth_jwt | `/api/auth/` | `register/`, `login/` (TokenObtainPair), `refresh/`, `me/` |
| catalog | `/api/catalog/` | `products/?search=&category=&ordering=&page=` |
| library | `/api/library/` | `authors/`, `books/`, `tags/` (routers, nested) |

UI:
| Página | Ruta |
|---|---|
| Landing | `/` |
| Demo CRUD | `/ui/crud/` |
| Demo Auth | `/ui/auth/` |
| Demo Catalog | `/ui/catalog/` |
| Demo Library | `/ui/library/` |

## Settings (cambios)

- `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` desde `.env` con `python-dotenv` y
  defaults seguros.
- **SQLite por defecto**; bloque MySQL/Postgres comentado como referencia.
- `INSTALLED_APPS`: registrar las 4 apps (`apps.crud`, etc.) + `django_filters`.
- `REST_FRAMEWORK`: JWT default auth, `DEFAULT_PERMISSION_CLASSES` AllowAny
  global (cada vista restringe lo suyo), paginación default
  (`PageNumberPagination`, page_size 5), filter backends por defecto.
- Django bump **4.0.5 → 4.2 LTS** (compat. Python 3.12).
- Borrar `storages`/boto3 (no se usan).

## requirements.txt objetivo

```
Django==4.2.16
djangorestframework==3.15.2
djangorestframework-simplejwt==5.3.1
django-filter==24.3
django-cors-headers==4.4.0
Pillow==10.4.0
python-dotenv==1.0.1
```

## Qué se borra

- `frontend/index.html` y todo `staticfiles/` (build React compilado + assets
  regenerables). `staticfiles/` se regenera con `collectstatic`; va a
  `.gitignore`.
- `base/` (app vieja con `Product` de solo lectura) — su modelo `Product`
  evoluciona dentro de `apps/catalog/`. Migración inicial nueva por app.
- `db.sqlite3` versionado — va a `.gitignore`.
- `base/signals.py` vacío.
- Dependencias basura: Flask, SQLAlchemy, cs50, Jinja2, gunicorn no usado, etc.

## Manejo de errores / calidad

- Cada vista devuelve códigos correctos (201 create, 204 delete, 404 not found,
  400 validation). FBV usa `get_object_or_404`.
- Tests por app: smoke test de cada endpoint (status + shape básica).
- Cada app trae `README.md` corto explicando el concepto y comandos `curl`.

## Plan de verificación

1. `venv` + `pip install -r requirements.txt`.
2. `python manage.py makemigrations && migrate` sin errores.
3. `python manage.py test` verde.
4. `python manage.py runserver` y smoke manual del landing + un endpoint.
5. Seed opcional vía management command o fixture para que las demos UI muestren
   datos.

## Fuera de alcance (YAGNI)

- React/SPA real, Docker, CI, deploy, websockets, throttling avanzado, tests
  exhaustivos de borde. El foco es claridad didáctica.
