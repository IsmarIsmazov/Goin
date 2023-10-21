from django.urls import path

from .views import banner_list

urlpatterns = [
    path('', banner_list)
]