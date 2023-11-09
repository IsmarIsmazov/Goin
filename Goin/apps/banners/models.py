from django.db import models

from apps.products.models import Category


# Create your models here.
class Banner(models.Model):
    image = models.ImageField(verbose_name='Изображение баннера')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='Категория баннера')

    def __str__(self):
        return f"Баннер для {self.category}"

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
