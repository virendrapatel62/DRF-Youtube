from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course , CourseSerializer

class CourseListView(APIView):
    def get(self , request ):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses , many = True)
        return Response(serializer.data)
    
    def post(self , request):
        courseSerializer = CourseSerializer(data = request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data , status=status.HTTP_201_CREATED)
        
        return Response(courseSerializer.errors)
        
