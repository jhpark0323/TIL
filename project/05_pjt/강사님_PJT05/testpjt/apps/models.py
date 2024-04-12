from django.db import models


class Article(models.Model):
    title = models.TextField()


class Query(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    keyword = models.TextField()
