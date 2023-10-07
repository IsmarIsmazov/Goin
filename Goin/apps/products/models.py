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
    weight = models.FloatField(verbose_name="Вес продукта")
    image = models.ImageField(verbose_name='Изображение продукта')
    available = models.BooleanField(verbose_name='Имеется в наличие')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория продукта")
    descriptions = models.TextField(verbose_name="Описание продукта")
    price = models.IntegerField(default=0, verbose_name="Цена продукта")
    discount = models.IntegerField(verbose_name="Скидка", null=True, blank=True)
    old_price = models.IntegerField(verbose_name='Старая цена', blank=True, null=True)
    popular = models.BooleanField(verbose_name='Популярная', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


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
