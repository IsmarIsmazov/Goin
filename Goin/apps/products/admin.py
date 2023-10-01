from django.contrib import admin

from .models import Product, ProductImages, Order, Category


class ProductImageInline(admin.TabularInline):
    model = ProductImages
    min_num = 1
    max_num = 20

    class Meta:
        model = ProductImages
        fields = '__all__'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "descriptions", "price")
    list_filter = ("title", "descriptions")
    search_fields = ("title", "descriptions")
    inlines = (ProductImageInline,)


admin.site.register(Order)
admin.site.register(Category)