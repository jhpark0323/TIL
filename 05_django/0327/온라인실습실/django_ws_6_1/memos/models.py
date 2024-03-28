from django.db import models

# Create your models here.
class Memo(models.Model):
    summary = models.CharField(max_length=20)
    memo = models.TextField()
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)