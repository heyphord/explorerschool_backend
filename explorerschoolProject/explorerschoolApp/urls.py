from django.contrib import admin
from django.urls import path
from .views import StudentAPIVIEW , StudentDetailsAPIVIEW , TutorAPIVIEW, TutorDetailsAPIVIEW,StudentToTutorAPIVIEW

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',StudentAPIVIEW.as_view()),
    path('student/<int:id>', StudentDetailsAPIVIEW.as_view()),
    path('tutors/',TutorAPIVIEW.as_view()),
    path('tutor/<int:id>', TutorDetailsAPIVIEW.as_view()),

    path('student-tuttor/assign/', StudentToTutorAPIVIEW.as_view()),
    
]