# Ejemplo 2 — Autenticación JWT

Demuestra un flujo de autenticación con **JSON Web Tokens** usando
`djangorestframework-simplejwt`: registrar un usuario, obtener un token,
renovarlo y acceder a un endpoint protegido.

## Endpoints

```
POST /api/auth/register/   crea usuario       {"username","email","password"}
POST /api/auth/login/      obtiene tokens      {"username","password"} -> {access, refresh}
POST /api/auth/refresh/    renueva access      {"refresh"} -> {access}
GET  /api/auth/me/         usuario actual      (header Authorization: Bearer <access>)
```

## Flujo con curl

```bash
# 1. Registrarse
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
     -d "username=ana&email=ana@example.com&password=Segura123!"

# 2. Login -> copiá el "access"
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
     -d "username=ana&password=Segura123!"

# 3. Endpoint protegido
curl http://127.0.0.1:8000/api/auth/me/ \
     -H "Authorization: Bearer <ACCESS_TOKEN>"
```

## Conceptos clave

- El **access token** es de vida corta (30 min); el **refresh** dura más (1 día).
  Se configuran en `SIMPLE_JWT` (ver `backend/settings.py`).
- `User.objects.create_user(...)` **hashea** la contraseña. Nunca la guardes en
  texto plano ni la devuelvas en la API (`write_only=True`).
- `permission_classes = [IsAuthenticated]` protege la vista: sin token válido
  devuelve `401`.
- El token va en el header `Authorization: Bearer <token>`.
