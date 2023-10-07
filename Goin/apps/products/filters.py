from django_filters import FilterSet
from django_filters import rest_framework as filters

from .models import Product


class ProductFilter(FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ("title", "category__name", "price")
