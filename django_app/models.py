from django.db import models
import uuid

class UserData(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userName = models.CharField(max_length=200, editable=False)
    weather_api = models.CharField(max_length=200)
    news_api = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
            ordering = ['-updated', '-created']
    def __str__(self):
        return self.userName + "   (" + str(self.user_id) + ")"
class Weather(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    weather_city = models.CharField(max_length=200, null=True)
    weather_country = models.CharField(max_length=200, null=True)
    weather_longitude = models.CharField(max_length=200, null=True)
    weather_latitude = models.CharField(max_length=200, null=True)
    use_coordinates = models.BooleanField(default=False)
    weather_file = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
            ordering = ['-updated', '-created']
    def __str__(self):
        return str(self.weather_city) + "   (" + str(self.user_id) + ")"
class News(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    news_file = models.CharField(max_length=200)
    news_providers = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
            ordering = ['-updated', '-created']
    def __str__(self):
        return self.news_providers + "   (" + str(self.user_id) + ")"