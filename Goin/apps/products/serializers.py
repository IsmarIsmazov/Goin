from rest_framework import serializers

from .models import Product, ProductImages, Order, Category


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ("image",)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImagesSerializer(many=True, read_only=False)
    category = CategorySerializer()

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        product = Product.objects.create(**validated_data)

        image_models = [
            ProductImages(product=product, **image)
            for image in images_data]
        ProductImages.objects.bulk_create(image_models)
        return product

    class Meta:
        model = Product
        fields = ("id", "title", "category", "descriptions", "created_at", "modified_at", "price", "images")


class OrderSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        queryset=Product.objects.all(),
        slug_field="title"
    )

    class Meta:
        model = Order
        fields = ('id', "username", "phone_number", "comment", "email",
                  "address", "payment_method", "delivery_method", "product")
