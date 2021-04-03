
from django.contrib import admin
from django.urls import path
from .app.views import employeeListView , employeeDetailView, UserListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employees',employeeListView),
    path('api/employees/<int:pk>',employeeDetailView),
    path('api/users',UserListView),
]
