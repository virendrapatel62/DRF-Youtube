
from django.contrib import admin
from django.urls import path
from .app.views import employeeListView , UserListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employees',employeeListView),
    path('api/users',UserListView),
]
