from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    phone = models.CharField(max_length=15, blank=True)
    department = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name