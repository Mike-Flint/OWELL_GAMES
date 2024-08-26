
from django.contrib import admin
from django.urls import path,include, re_path
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('BoxStorm/', include('Box_Storm.urls')),
    path('SamuraiHonor/', include('Samurai_Honor.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api/', include('API.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

def custom_404(request, exception):

    return HttpResponse("<div style='position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 30px; text-align: center;'><h1>Error 404 </h1><h4>This path does not exist</h4></div>", status=404)

handler404 = custom_404