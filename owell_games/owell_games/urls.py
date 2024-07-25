
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('BoxStorm/', include('Box_Storm.urls')),
    path('SamuraiHonor/', include('Samurai_Honor.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api/', include('API.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
