from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import router as users_api_router

admin.site.site_header = "Global Service"
auth_api_urls=[
    path(r'', include('drf_social_oauth2.urls', namespace='drf'))
]

if settings.DEBUG:
    auth_api_urls.append(path(r'verify/', include('rest_framework.urls')))


api_url_patterns = [
    path (r'auth/', include(auth_api_urls)),
    path(r'accounts/', include(users_api_router.router.urls)),
    path(r'customers/', include('Customer.urls')),
]

urlpatterns = [


    path('admin/', admin.site.urls),
    path('api/', include(api_url_patterns)),
    # path("", include("django_nextjs.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)