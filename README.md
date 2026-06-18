# Django API — Laboratorio de práctica

Proyecto para **aprender a construir APIs con Django REST Framework** a través de
ejemplos aislados. Cada concepto vive en su propia app bajo `apps/`, con su
código, sus tests y su `README.md` explicativo. Incluye además **plantillas de
UI** (templates Django) que consumen cada API.

Todo separado y organizado: podés estudiar un ejemplo a la vez sin que se mezcle
con los demás.

## Ejemplos incluidos

| # | App | Concepto | API | Demo UI |
|---|-----|----------|-----|---------|
| 1 | [`apps/crud`](apps/crud/README.md) | CRUD en 3 estilos (FBV, generics, ViewSet) | `/api/crud/` | `/ui/crud/` |
| 2 | [`apps/auth_jwt`](apps/auth_jwt/README.md) | Autenticación JWT (registro, login, refresh, protegido) | `/api/auth/` | `/ui/auth/` |
| 3 | [`apps/catalog`](apps/catalog/README.md) | Paginación + filtros + búsqueda + ordenamiento | `/api/catalog/` | `/ui/catalog/` |
| 4 | [`apps/library`](apps/library/README.md) | Relaciones FK/M2M + nested serializers + upload de imagen | `/api/library/` | `/ui/library/` |

Cada API se puede explorar también con el **API navegable** de DRF
(abrí la URL en el navegador).

## Estructura

```
django-api/
├── backend/            configuración del proyecto (settings, urls, vistas de UI)
├── apps/               un ejemplo aislado por carpeta
│   ├── crud/           cada app: models, serializers, views, urls, tests, README
│   ├── auth_jwt/
│   ├── catalog/
│   ├── library/
│   └── core/           comando seed_demo (datos de ejemplo)
├── templates/          UI server-rendered (base + landing + una demo por ejemplo)
├── static/css/         estilos compartidos
└── docs/               diseño del proyecto
```

## Cómo correr

Requiere **Python 3.10+**.

```bash
# 1. Entorno virtual e instalación
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2. (Opcional) Variables de entorno
cp .env.example .env               # editá SECRET_KEY / DEBUG si querés

# 3. Base de datos (SQLite por defecto, sin configuración)
python manage.py migrate

# 4. Datos de ejemplo para las demos
python manage.py seed_demo

# 5. (Opcional) Usuario admin
python manage.py createsuperuser

# 6. Levantar el servidor
python manage.py runserver
```

Abrí <http://127.0.0.1:8000/> para ver el índice de ejemplos.

## Tests

```bash
python manage.py test            # todos
python manage.py test apps.crud  # un ejemplo
```

## Cómo agregar tu propio ejemplo

1. Creá una app en `apps/mi_ejemplo/` (con `apps.py` cuyo `name = "apps.mi_ejemplo"`).
2. Registrala en `INSTALLED_APPS` (`backend/settings.py`).
3. Montá sus URLs en `backend/urls.py` bajo `/api/mi_ejemplo/`.
4. Agregá un `README.md` que explique el concepto y tests en `tests.py`.

## Stack

Django 4.2 LTS · Django REST Framework · djangorestframework-simplejwt ·
django-filter · Pillow · python-dotenv · django-cors-headers.

## Notas de configuración

- **SQLite** por defecto para arrancar sin fricción. En `backend/settings.py`
  hay bloques comentados para MySQL y Postgres.
- Los **secrets** (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`) se leen del `.env`
  (que está en `.gitignore`). Hay defaults seguros para desarrollo.
- DRF usa **AllowAny** global para que el API navegable funcione; las vistas que
  necesitan protección lo declaran explícitamente (ver `apps/auth_jwt`).
