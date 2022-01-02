"""mess URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from mess import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signin, name='signin'),
    path('home/', views.home),
    path('accesscoupon/', views.accesscoupon),
    path('buycoupon/', views.buycoupon),
    path('complaintstatus/', views.complaintstatus),
    path('messmenu/', views.messmenu),
    path('menumon/', views.menumon),
    path('menutue/', views.menutue),
    path('menuwed/', views.menuwed),
    path('menuthu/', views.menuthu),
    path('menufri/', views.menufri),
    path('menusat/', views.menusat),
    path('menusun/', views.menusun),
    path('messschedule/', views.messschedule),
    path('registercomplaint/', views.registercomplaint),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)