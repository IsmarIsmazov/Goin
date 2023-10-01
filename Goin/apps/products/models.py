from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .constants import PAYMENT_METHOD, DELIVERY_METHOD


class Category(models.Model):
    name = models.CharField(max_length=120, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    title = models.CharField(max_length=155, verbose_name="Название продукта")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория продукта")
    descriptions = models.TextField(verbose_name="Описание продукта")
    price = models.IntegerField(default=0, verbose_name="Цена продукта")
    created_at = models.DateField(auto_now=True, verbose_name="Дата создание продукта")
    modified_at = models.DateField(auto_now_add=True, verbose_name="Дата изменение продукта")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductImages(models.Model):
    image = models.ImageField(verbose_name="Фотография продукта")
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name="images", null=True, blank=True)

    class Meta:
        verbose_name = "Изображения продукта"
        verbose_name_plural = "Изображении продукта"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name="Продукт")
    username = models.CharField(max_length=155, verbose_name="Имя клиента")
    email = models.EmailField(verbose_name="Почта клиента")
    address = models.CharField(max_length=255, verbose_name="Адрес клиента")
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD, verbose_name="Способ оплаты")
    delivery_method = models.CharField(max_length=50, choices=DELIVERY_METHOD, verbose_name="Способ доставки")
    phone_number = PhoneNumberField(verbose_name="Номер телефона клиента")
    comment = models.TextField(verbose_name="Комментария к заказу")

    def __str__(self):
        return self.email, self.username

    class Meta:
        verbose_name = "Заказать продукт"
        verbose_name_plural = "Заказанные продкуты"
