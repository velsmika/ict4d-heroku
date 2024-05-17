"""
URL configuration for ict4d project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menuAudio/<str:lang>/<str:name>/', views.get_menu_audio),
    path('uploadfile', views.upload_file_menu),
    path('uploadfilefarmer', views.upload_file_farmer),
    path('farmeraudio/<str:lang>/', views.get_amount_farmer_audio_seedtype),
    path('farmeraudio/<str:lang>/<int:id>', views.get_farmer_audio),
]
