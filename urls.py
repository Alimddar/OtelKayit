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
from OtelApp import views

baseapiUrl = "api/v1/"

urlpatterns = [
    # Sayfa Pathleri
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('otel', otel, name="oteldashboard"),
    path('blokaj', blokaj, name="blok"),
    path('muhasebe', muhasebe, name="muhasebe"),
    path('odadetay/<odaId>', detailroom, name="odadetay"),
    path('musteridetay/<musteriId>', detailguest, name="musteridetay"),
    path('logout', logoutUser ,name="logout"),
    path('create-reservation/', views.create_reservation, name='create_reservation'),
    path('view-reservations/', views.view_reservations, name='view_reservations'),

    # Api Path burada!
    path(f'{baseapiUrl}odadetay/<odaId>', guestregister, name="misafirkayit"),
    path(f'{baseapiUrl}roomadd',roomadd, name="roomadd"),
    path(f'{baseapiUrl}roomdelete/<odaId>', roomdelete, name="roomdelete"),

    # 404 Path'idir!.
    re_path(r'^.*/$', hatasayfasi, name="404"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)