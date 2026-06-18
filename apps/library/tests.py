from rest_framework import status
from rest_framework.test import APITestCase

from .models import Author, Book, Tag


class LibraryTests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Cortázar")
        self.tag = Tag.objects.create(name="ficción")

    def test_create_book_with_relations(self):
        resp = self.client.post(
            "/api/library/books/",
            {
                "title": "Rayuela",
                "author_id": self.author.id,
                "tag_ids": [self.tag.id],
                "published_year": 1963,
            },
            format="json",
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        # La respuesta trae el autor anidado, no solo el id.
        self.assertEqual(resp.data["author"]["name"], "Cortázar")
        self.assertEqual(resp.data["tags"][0]["name"], "ficción")

        book = Book.objects.get(title="Rayuela")
        self.assertEqual(book.author, self.author)
        self.assertIn(self.tag, book.tags.all())

    def test_author_detail_includes_books(self):
        book = Book.objects.create(title="Bestiario", author=self.author)
        resp = self.client.get(f"/api/library/authors/{self.author.id}/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        titles = [b["title"] for b in resp.data["books"]]
        self.assertIn(book.title, titles)

    def test_author_list_has_no_books_field(self):
        resp = self.client.get("/api/library/authors/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        first = resp.data["results"][0] if "results" in resp.data else resp.data[0]
        self.assertNotIn("books", first)
