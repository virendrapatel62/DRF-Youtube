
from django.contrib import admin
from django.urls import path, include
# from CBVapp.views import CourseListView , CourseDetailView

from rest_framework.routers import DefaultRouter
from CBVapp.views import CourseViewSet

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='course')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
