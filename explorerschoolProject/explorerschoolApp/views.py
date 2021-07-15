from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView
from .models import Student , Tutor
from .serializers import StudentSerializer

# Create your views here.

class StudentAPIVIEW(APIView):
    
    def get( self, request):
        students = Student.objects.all()
        serializer = StudentSerializer( students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status =status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailsAPIVIEW(APIView):
    def getStudentById(self, id):
        try:
            return Student.objects.get(id=id)

        except Student.DoesNotExist:
            return Response( status =status.HTTP_404_NOT_FOUND)


    def get(self, request, id):
        student = self.getStudentById(id)
        serializer = StudentSerializer(student, request.data)
        return Response(serializer.data)


    def put(self, request, id):
        student = self.getStudentById(id)
        serializer = StudentSerializer(student)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status =status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = self.getStudentById(id)
        student.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)