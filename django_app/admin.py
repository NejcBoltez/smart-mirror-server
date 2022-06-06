from django.contrib import admin

from .models import Weather, News

admin.site.register(Weather)
admin.site.register(News)