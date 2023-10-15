from django.db import models
import uuid

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userName = models.CharField(max_length=200, unique=True)
    userPassword = models.CharField(max_length=200, unique=True)
    weather_api = models.CharField(max_length=200)
    weather = models.CharField(max_length=200)
    news_api = models.CharField(max_length=200)
    news = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
            ordering = ['-updated', '-created']
    def __str__(self):
        return self.name + "   (" + str(self.user_id) + ")"