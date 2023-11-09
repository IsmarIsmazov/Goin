from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from .settings.yasg import urlpatterns_swagger as doc_urls

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/products/', include("apps.products.urls")),
                  path('api/v1/recommendation/', include("apps.recommendation.urls")),
                  path('api/v1/banners/', include("apps.banners.urls"))

              ] + doc_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
