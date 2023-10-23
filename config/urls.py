from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Test. User Auth",
        default_version='v1',
        description="Users Auth",
        contact=openapi.Contact(email="eralideveloper@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('app.urls')),
    path('api/v1/products/', include('products.urls')),
    path('api/v1/pay/', include('billing.urls')),
    path('api/v1/cloudinary/', include('cloud_inary.urls')),
    path('api/v1/proxy/', include('proxyapp.urls')),
    path('api/v1/sms-auth/', include('custom_auth.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    # path('api/v1/custom-auth/', include('djoser.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/v1/custom-auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/custom-auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/custom-auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
