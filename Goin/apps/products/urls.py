from django.urls import path

from .views import product_list, product_detail, order_post, category_list, popular_products

urlpatterns = [
    path('', product_list),
    path('<int:pk>/', product_detail),
    path('order/', order_post),
    path('popular-products/', popular_products),
    path('category/', category_list, )
]
