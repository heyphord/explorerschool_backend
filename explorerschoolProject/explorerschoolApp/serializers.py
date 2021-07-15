from rest_framework import serializers
from .models import Student,Tutor

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields ='__all__'


class TutorSerializer(serializers.ModelSerializer):
    students= StudentSerializer(many=True, read_only=True )
    class Meta:
        model = Tutor
        fields ='__all__'

    

