from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('auth/', include('djoser.urls')), #added
    path('auth/', include('djoser.urls.jwt')), #added

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #added
