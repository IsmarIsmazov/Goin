from rest_framework import serializers

from .models import Recommendation
from ..products.serializers import ProductSerializer


class RecommendationSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Recommendation
        fields = ("id", "product")
