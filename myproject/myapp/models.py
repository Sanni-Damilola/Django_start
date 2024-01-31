from django.db import models

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField()
    bioGraphy = models.TextField()

    def __str__(self) -> str:
        return f"{self.firstName}{self.lastName}"
        