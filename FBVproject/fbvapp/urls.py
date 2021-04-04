
from django.contrib import admin
from django.urls import path
from .views import courseListView , courseDetailView

urlpatterns = [
    path('courses', courseListView),
    path('courses/<int:pk>', courseDetailView),
]
