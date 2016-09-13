from __future__ import unicode_literals

from django.db import models

# Create your models here.



# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=32)
    content = models.TextField()