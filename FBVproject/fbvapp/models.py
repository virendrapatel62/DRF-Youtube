from django.db import models
from rest_framework import serializers
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=40)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    duration= models.FloatField()

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields ="__all__"