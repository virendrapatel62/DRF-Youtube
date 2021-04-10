
from django.contrib import admin
from django.urls import path , include
from CBVapp.views import CourseListView , CourseDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('CBVapp.urls'))
]
