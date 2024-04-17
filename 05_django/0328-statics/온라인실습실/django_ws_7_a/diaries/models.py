from django.db import models

# Create your models here.
class Diary(models.Model):
    content = models.TextField(max_length=125)
    created_at = models.DateField(auto_now_add=True)