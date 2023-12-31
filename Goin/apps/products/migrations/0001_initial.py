# Generated by Django 4.2.5 on 2023-11-07 07:33

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название категории')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, unique=True, verbose_name='Название продукта')),
                ('weight', models.FloatField(verbose_name='Вес продукта')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение продукта')),
                ('available', models.BooleanField(verbose_name='Имеется в наличие')),
                ('in_warehouse', models.IntegerField(verbose_name='Количество товаров в складе')),
                ('descriptions', models.TextField(verbose_name='Описание продукта')),
                ('price', models.IntegerField(default=0, verbose_name='Цена продукта')),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name='Скидка')),
                ('old_price', models.IntegerField(blank=True, null=True, verbose_name='Старая цена')),
                ('popular', models.BooleanField(blank=True, default=False, null=True, verbose_name='Популярная')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Категория продукта')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=155, verbose_name='Имя клиента')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес клиента')),
                ('payment_method', models.CharField(choices=[('Оплата наличными', 'Оплата наличными'), ('Оплата переводом', 'Оплата переводом')], max_length=50, verbose_name='Способ оплаты')),
                ('delivery_method', models.CharField(choices=[('Самовывоз', 'Самовывоз'), ('Доставка к дому', 'Доставка к дому')], max_length=50, verbose_name='Способ доставки')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Номер телефона клиента')),
                ('comment', models.TextField(verbose_name='Комментария к заказу')),
                ('product', models.ManyToManyField(to='products.product', verbose_name='Продукты')),
            ],
            options={
                'verbose_name': 'Заказать продукт',
                'verbose_name_plural': 'Заказанные продкуты',
            },
        ),
    ]
