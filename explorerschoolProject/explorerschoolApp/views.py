from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView
from .models import Student , Tutor
from .serializers import StudentSerializer, TutorSerializer

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
   

    def get(self,request, id):
        try:
            student =Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)

        except Student.DoesNotExist:
            return Response( "Student with id does not exist",status =status.HTTP_404_NOT_FOUND)
        


    def put(self, request, id):
        try:
            student =Student.objects.get(id=id)
            serializer = StudentSerializer(student, request.data)

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response(serializer.data, status =status.HTTP_201_CREATED)

        except Student.DoesNotExist:
            return Response( "Student with id does not exist",status =status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            student =Student.objects.get(id=id)
            student.delete()
            return Response("Deleted successfulyy",status = status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response("Student with id does not exist",status = status.HTTP_404_NOT_FOUND)


class TutorAPIVIEW(APIView):

    def get( self, request):
        tutors = Tutor.objects.all()
        serializer = TutorSerializer( tutors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TutorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status =status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TutorDetailsAPIVIEW(APIView):
   

    def get(self,request, id):
        try:
            tutor =Tutor.objects.get(id=id)
            serializer = TutorSerializer(tutor)
            return Response(serializer.data)

        except Tutor.DoesNotExist:
            return Response( "Tutor with id does not exist",status =status.HTTP_404_NOT_FOUND)
        


    def put(self, request, id):
        try:
            tutor =Tutor.objects.get(id=id)
            serializer = TutorSerializer(tutor, request.data)

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response(serializer.data, status =status.HTTP_201_CREATED)

        except Tutor.DoesNotExist:
            return Response( "Tutor with id does not exist",status =status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            tutor =Tutor.objects.get(id=id)
            tutor.delete()
            return Response("Deleted successfulyy",status = status.HTTP_204_NO_CONTENT)
        except Tutor.DoesNotExist:
            return Response("Tutor with id does not exist",status = status.HTTP_404_NOT_FOUND)


#assign student to tutors
class StudentToTutorAPIVIEW(APIView):

    

    def post(self, request):
        
        # return Response(request.data['tutor_id'],status = status.HTTP_404_NOT_FOUND)
        try:
            tutor =Tutor.objects.get(id=request.data['tutor_id'])
            student = Student.objects.get(id = request.data['student_id'])
            tutor.students.add(student)
            tutor.save()
            serializer = TutorSerializer(tutor)
            return Response(serializer.data,status = status.HTTP_200_OK)

        except Tutor.DoesNotExist: 
            return Response("Tutor with id does not exist",status = status.HTTP_404_NOT_FOUND)
            
        except Student.DoesNotExist: 
            return Response("Student with id does not exist",status = status.HTTP_404_NOT_FOUND)

       
