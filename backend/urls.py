"""Rutas raíz del proyecto.

- `/`            landing con el índice de ejemplos
- `/ui/...`      demos de UI (templates Django que consumen las APIs)
- `/api/<ej>/`   cada ejemplo de API montado bajo su propio prefijo
- `/admin/`      admin de Django
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from backend import ui_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # UI (server-rendered)
    path("", ui_views.index, name="index"),
    path("ui/crud/", ui_views.crud, name="ui-crud"),
    path("ui/auth/", ui_views.auth, name="ui-auth"),
    path("ui/catalog/", ui_views.catalog, name="ui-catalog"),
    path("ui/library/", ui_views.library, name="ui-library"),

    # APIs — un ejemplo por app
    path("api/crud/", include("apps.crud.urls")),
    path("api/auth/", include("apps.auth_jwt.urls")),
    path("api/catalog/", include("apps.catalog.urls")),
    path("api/library/", include("apps.library.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
