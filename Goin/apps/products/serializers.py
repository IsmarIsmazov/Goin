from rest_framework import serializers

from .models import Product, Order, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = (
            "id", 'weight', "title", 'available', "category", "descriptions", "in_warehouse", "price", "image",
            'discount',
            'old_price', 'popular',)


class OrderSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        queryset=Product.objects.all(),
        slug_field="title"
    )

    class Meta:
        model = Order
        fields = ('id', "username", "phone_number", "comment", "email",
                  "address", "payment_method", "delivery_method", "product")
