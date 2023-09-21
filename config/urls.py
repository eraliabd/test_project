from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('app.urls')),
    path('api/v1/products/', include('products.urls')),
    path('api/v1/pay/', include('billing.urls')),
    path('api/v1/cloudinary/', include('cloud_inary.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
