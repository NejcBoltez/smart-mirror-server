from django.contrib import admin

from .models import Weather, News, APIkeys

admin.site.register(Weather)
admin.site.register(News)
admin.site.register(APIkeys)