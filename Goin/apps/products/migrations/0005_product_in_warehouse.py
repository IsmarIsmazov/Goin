# Generated by Django 4.2.5 on 2023-10-21 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_available_product_discount_product_old_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_warehouse',
            field=models.IntegerField(default=1, verbose_name='Количество товаров в складе'),
            preserve_default=False,
        ),
    ]