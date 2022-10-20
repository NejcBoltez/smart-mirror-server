
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name="home"),
    path('news', views.NewsPage, name="news"),
    path('weather', views.WeatherPage, name="weather"),
    path('user_profile', views.UserPage, name="user_prop"),
]
