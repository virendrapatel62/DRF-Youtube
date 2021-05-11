
from django.shortcuts import render
from rest_framework import generics
from .serializers import InstructorSerializer, CourseSerializer
from .models import Instructor, Course


class InstructorListView(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()


class CourseListView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
