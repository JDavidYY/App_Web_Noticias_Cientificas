"""Divulgadores_Hiperactivos_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from core import views as views_core
from . import settings
from ciencia import views as views_ciencia
from cultura import views as views_cultura
from entretenimiento import views as views_entretenimiento
from psicologia import views as views_psicologia

urlpatterns = [
    path('', views_core.home, name="home"),
    path('ciencia/', views_ciencia.ciencia, name="ciencia"),
    path('cultura/', views_cultura.cultura, name="cultura"),
    path('entretenimiento/', views_entretenimiento.entretenimiento, name="entretenimiento"),
    path('psicologia/', views_psicologia.psicologia, name="psicologia"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)