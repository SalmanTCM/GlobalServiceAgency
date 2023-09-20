from django.contrib import admin
from django.urls import path, include
admin.site.site_header = "Global Service"
urlpatterns = [


    path('admin/', admin.site.urls),

    path('api/', include('Customer.urls')),
    # path("", include("django_nextjs.urls")),
]
