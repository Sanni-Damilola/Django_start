from django.db import models

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(maxlength=100)
    desciption = models.TextField()