"""
URL configuration for OtelKayit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Static Path
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, re_path

# View çek
from OtelApp.views import *
from OtelAppApi.views import *


urlpatterns = [
    # Sayfa Pathleri
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('otel', otel, name="oteldashboard"),
    path('blokaj', blokaj, name="blok"),
    path('muhasebe', muhasebe, name="muhasebe"),
    path('odadetay/<odaId>', detailroom, name="odadetay"),

    # Api Path burada!
    path('api/v1/odadetay/<odaId>', guestregister, name="misafirkayit"),

    # 404 Path'idir!.
    re_path(r'^.*/$', hatasayfasi, name="404"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
