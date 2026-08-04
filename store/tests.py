from django.test import TestCase
from django.urls import reverse

from .models import Category, Product


class ProductCatalogTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Tech")
        self.product = Product.objects.create(
            category=self.category,
            name="Clavier RGB",
            description="Un clavier moderne et rapide.",
            price=49.99,
            is_active=True,
        )
        self.inactive_product = Product.objects.create(
            category=self.category,
            name="Casque sans fil",
            description="Produit inactif pour le test.",
            price=89.90,
            is_active=False,
        )

    def test_home_page_shows_active_products(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Clavier RGB")
        self.assertNotContains(response, "Casque sans fil")

    def test_search_filter_works(self):
        response = self.client.get(reverse("home"), {"q": "clavier"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Clavier RGB")

    def test_product_detail_page(self):
        response = self.client.get(reverse("product_detail", args=[self.product.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Clavier RGB")
        self.assertContains(response, "Un clavier moderne et rapide.")
