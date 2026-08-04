from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nom",
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Catégorie",
    )

    name = models.CharField(
        max_length=150,
        verbose_name="Nom",
    )

    description = models.TextField(
        verbose_name="Description",
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Prix",
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
        verbose_name="Image",
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Produit visible",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de création",
    )

    def __str__(self):
        return self.name