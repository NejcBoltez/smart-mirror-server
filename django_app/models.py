from django.db import models



class Weather(models.Model):
    #host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    coordX = models.CharField(max_length=200)
    coordY = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants = models.ManyToManyField(
    #    User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class News(models.Model):
    #host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
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
        return self.name