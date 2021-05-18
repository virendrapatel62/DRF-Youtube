
from django.contrib import admin
from django.urls import path
from .views import CourseDetailView, CourseListView, InstructorDetailView, InstructorListView
urlpatterns = [
    path('instructors/', InstructorListView.as_view()),
    path('courses/', CourseListView.as_view()),
    path('courses/<int:pk>', CourseDetailView.as_view(), name='course-detail'),
    path('instructors/<int:pk>', InstructorDetailView.as_view(),
         name='instructor-detail')
]
