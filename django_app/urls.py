"""smartmirror_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
    path('', views.homePage, name="home"),
    path('news', views.NewsPage, name="news"),
    path('weather', views.WeatherPage, name="weather"),
    path('user_profile', views.UserPage, name="user_prop"),
    path('new_user', views.NewUserPage, name="new_user"),
    path('login', views.LoginPage, name="user_login")
]
