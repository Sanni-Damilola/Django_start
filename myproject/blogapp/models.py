from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    excerpt = models.CharField(max_length=200)
    content = models.TextField()