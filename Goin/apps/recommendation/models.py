from django.db import models

from apps.products.models import Product


# Create your models here.
class Recommendation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")

    def __str__(self):
        return f" {self.product.title}"

    class Meta:
        verbose_name = "Рекомендация"
        verbose_name_plural = "Рекомендации"
