
from django.contrib import admin
from django.urls import path
from .views import CourseListView, InstructorListView
urlpatterns = [
    path('instructors', InstructorListView.as_view()),
    path('courses', CourseListView.as_view())
]
