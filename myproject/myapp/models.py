from django.db import models

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField()
    bioGraphy = models.TextField()

    def __str__(self) -> str:
        return f"{self.firstName}{self.lastName}"
        


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.name}"
    

class Course(models.Model):
    title = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name ="courses")

    def __str__(self) -> str:
        return f"{self.title}"
    
