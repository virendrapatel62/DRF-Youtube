
from django.contrib import admin
from django.urls import path
from CBVapp.views import CourseListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("test" , CourseListView.as_view())
]
