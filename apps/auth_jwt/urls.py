"""Rutas del ejemplo de autenticación JWT.

- POST /api/auth/register/   crea usuario
- POST /api/auth/login/      obtiene access + refresh token
- POST /api/auth/refresh/    renueva el access token
- GET  /api/auth/me/         devuelve el usuario actual (requiere token)
"""
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import MeView, RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="auth-register"),
    path("login/", TokenObtainPairView.as_view(), name="auth-login"),
    path("refresh/", TokenRefreshView.as_view(), name="auth-refresh"),
    path("me/", MeView.as_view(), name="auth-me"),
]
