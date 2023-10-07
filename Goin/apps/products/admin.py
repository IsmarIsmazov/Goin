from django.contrib import admin

from .models import Product, Order, Category




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "descriptions", "price")
    list_filter = ("title", "descriptions")
    search_fields = ("title", "descriptions")


admin.site.register(Order)
admin.site.register(Category)
