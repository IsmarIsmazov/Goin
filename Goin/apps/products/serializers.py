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
        slug_field="title",
        many=True
    )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = ', '.join(representation['product'])
        return representation

    class Meta:
        model = Order
        fields = ('id', "username", "phone_number", "comment",
                  "address", "payment_method", "delivery_method", "product")
