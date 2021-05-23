
from django.contrib import admin
from django.urls import path
from .views import CourseDetailView, CourseListView, InstructorDetailView, InstructorListView
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('instructors/', InstructorListView.as_view()),
    path('courses/', CourseListView.as_view()),
    path('courses/<int:pk>', CourseDetailView.as_view(), name='course-detail'),
    path('instructors/<int:pk>', InstructorDetailView.as_view(),
         name='instructor-detail'),


    path('auth/login/', TokenObtainPairView.as_view(),
         name='create-token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
