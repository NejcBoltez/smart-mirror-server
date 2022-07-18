from django.db import models
import uuid

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)
    weather_api = models.CharField(max_length=200)
    news_api = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
            ordering = ['-updated', '-created']
    def __str__(self):
        return self.name + "   (" + str(self.user_id) + ")"

class Weather(models.Model):
    user_fik = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    coordX = models.CharField(max_length=200)
    coordY = models.CharField(max_length=200)
    #description = models.TextField(null=True, blank=True)
    #participants = models.ManyToManyField(
    #    User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.country + ', ' + self.city

class News(models.Model):
    user_fik = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    news_to_select = models.CharField(max_length=200)
    '''city = models.CharField(max_length=200)
    coordX = models.CharField(max_length=200)
    coordY = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)'''
    #participants = models.ManyToManyField(
    #    User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return str(self.news_to_select)

