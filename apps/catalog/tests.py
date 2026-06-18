from decimal import Decimal

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Product


class CatalogTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(7):
            Product.objects.create(
                name=f"Producto {i}",
                category="tech" if i % 2 else "home",
                price=Decimal("10.00") * (i + 1),
                stock=0 if i == 0 else i,
            )

    def test_pagination(self):
        resp = self.client.get("/api/catalog/products/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # PAGE_SIZE = 5 -> 5 en la primera página, count total 7
        self.assertEqual(resp.data["count"], 7)
        self.assertEqual(len(resp.data["results"]), 5)
        self.assertIsNotNone(resp.data["next"])

    def test_filter_category(self):
        resp = self.client.get("/api/catalog/products/?category=tech")
        self.assertTrue(all(p["category"] == "tech" for p in resp.data["results"]))

    def test_filter_price_range(self):
        resp = self.client.get("/api/catalog/products/?min_price=30&max_price=50")
        for p in resp.data["results"]:
            self.assertGreaterEqual(Decimal(p["price"]), Decimal("30"))
            self.assertLessEqual(Decimal(p["price"]), Decimal("50"))

    def test_in_stock(self):
        resp = self.client.get("/api/catalog/products/?in_stock=true")
        self.assertTrue(all(p["stock"] > 0 for p in resp.data["results"]))

    def test_search(self):
        resp = self.client.get("/api/catalog/products/?search=Producto 3")
        self.assertGreaterEqual(resp.data["count"], 1)

    def test_ordering(self):
        resp = self.client.get("/api/catalog/products/?ordering=price")
        prices = [Decimal(p["price"]) for p in resp.data["results"]]
        self.assertEqual(prices, sorted(prices))
