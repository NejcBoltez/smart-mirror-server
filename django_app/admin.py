from django.contrib import admin

from .models import UserData, Weather, News

admin.site.register(UserData)
admin.site.register(Weather)
admin.site.register(News)