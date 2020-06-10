from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=64, null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

class Course(models.Model):
    name = models.CharField(max_length=255, null=True)
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=1000, null = True)