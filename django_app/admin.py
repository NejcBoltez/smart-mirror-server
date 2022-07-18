from django.contrib import admin

from .models import User, Weather, News

admin.site.register(Weather)
admin.site.register(News)
admin.site.register(User)