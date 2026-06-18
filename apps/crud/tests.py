from rest_framework import status
from rest_framework.test import APITestCase

from .models import Task


class CrudTests(APITestCase):
    def test_create_and_list_fbv(self):
        resp = self.client.post("/api/crud/tasks/", {"title": "Aprender DRF"})
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

        resp = self.client.get("/api/crud/tasks/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)

    def test_update_and_delete_fbv(self):
        task = Task.objects.create(title="Pendiente")
        resp = self.client.patch(
            f"/api/crud/tasks/{task.pk}/", {"done": True}, format="json"
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(Task.objects.get(pk=task.pk).done)

        resp = self.client.delete(f"/api/crud/tasks/{task.pk}/")
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_viewset_crud(self):
        resp = self.client.post(
            "/api/crud/tasks-viewset/", {"title": "Vía viewset"}
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_detail_404(self):
        resp = self.client.get("/api/crud/tasks/999/")
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)
