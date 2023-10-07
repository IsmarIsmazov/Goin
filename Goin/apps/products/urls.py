from django.urls import path

from .views import product_list, product_detail, order_post, category_list

urlpatterns = [
    path('', product_list),
    path('<int:pk>/', product_detail),
    path('order/', order_post, name='order-post'),
    path('category/', category_list,)
]
