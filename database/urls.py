"""database URL Configuration

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
from django.contrib.gis import admin
from django.urls import path
from data import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('data/', views.data, name='data')
]

admin.site.site_header = "Solidarity administration"
admin.site.site_title = "Solidarity Import Database"
admin.site.index_title = "Welcome to Solidarity Import Database"
