from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    department = models.CharField(max_length=40)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.first_name


class Tutor(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    students = models.ManyToManyField(Student)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.first_name

    