from django.contrib import admin
from django.urls import path
from .views import StudentAPIVIEW , StudentDetailsAPIVIEW

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',StudentAPIVIEW.as_view()),
    path('student/<int:id>', StudentDetailsAPIVIEW.as_view()),
    
]