from django.db import models

# Create your models here.

class Student(models.Model):
    stu_name = models.CharField(max_length = 250)
    stu_address= models.TextField()