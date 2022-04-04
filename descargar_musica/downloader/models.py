from django.db import models

# Create your models here.

class VideoLinks(models.Model):
    link = models.CharField(max_length=200)