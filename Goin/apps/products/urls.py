from django.urls import path

from .views import product_list, product_detail, order_post

urlpatterns = [
    path('products/', product_list),
    path('products/<int:pk>/', product_detail),
    path('order/', order_post, name='order-post'),
]
