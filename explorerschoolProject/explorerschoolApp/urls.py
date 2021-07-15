from django.contrib import admin
from django.urls import path
from .views import StudentAPIVIEW , StudentDetailsAPIVIEW

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', StudentDetailsAPIVIEW.as_view()),
    path('student-details/<int:id>', StudentAPIVIEW.as_view()),
    
]