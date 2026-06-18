from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class AuthJwtTests(APITestCase):
    def test_register(self):
        resp = self.client.post(
            "/api/auth/register/",
            {"username": "ana", "email": "ana@example.com", "password": "Segura123!"},
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="ana").exists())
        self.assertNotIn("password", resp.data)

    def test_login_and_me(self):
        User.objects.create_user(username="ana", password="Segura123!")

        resp = self.client.post(
            "/api/auth/login/", {"username": "ana", "password": "Segura123!"}
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        token = resp.data["access"]

        # Sin token -> 401
        resp = self.client.get("/api/auth/me/")
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

        # Con token -> 200
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        resp = self.client.get("/api/auth/me/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["username"], "ana")
