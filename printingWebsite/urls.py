from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django .conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('', include('bannaoapp.urls')),
    path('admin/', admin.site.urls),
    
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    
]
