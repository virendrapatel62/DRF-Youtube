from django.db import models


class Instructor(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.email


class Course(models.Model):
    title = models.CharField(max_length=30)
    rating = models.IntegerField()
    instructor = models.ForeignKey(
        Instructor, on_delete=models.CASCADE, related_name='courses')
