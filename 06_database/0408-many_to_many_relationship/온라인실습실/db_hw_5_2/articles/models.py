# articles/models.py
from django.db import models
from django.conf import settings 

class Article(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
  title = models.TextField()
  content = models.TextField()