from django.test import TestCase
from django.test import Client
from .models import Tutor ,Student
# Create your tests here.

class TutorTestCase(TestCase):
    def test_get_tutors(self):
        c = Client()
        response = c.get('/tutors/')
        self.assertEqual(response.status_code, 200)
        
    def test_get_tutor(self):
        tutor = Tutor( first_name ="Hayford", last_name="Ansah",  email="o.ansah.hayford@gmail.com")
        tutor.save()

        c = Client()
        response = c.get('/tutor/'+ str(tutor.id))
        self.assertEqual(response.status_code, 200)
        
    def test_create_tutor(self):
        
        c = Client()
        response = c.post('/tutors/' ,
        {
            "first_name": "hayford2",
            "last_name" : "ansah2",
            "email":"hayford2@gamil.com"

        })
        self.assertEqual(response.status_code, 201)
        
    def test_edit_tutor(self):
        tutor = Tutor( first_name ="Hayford", last_name="Ansah",  email="o.ansah.hayford@gmail.com")
        tutor.save()

        c = Client()
        response = c.put('/tutor/'+ str( tutor.id) ,
        {
            "first_name": "hayfordEdited",
            "last_name" : "ansahEdited",
            "email":"hayford@gamil.com"

        },
        content_type='application/json')
        # print( response.content)
        self.assertEqual(response.status_code, 201)
        
    def test_delete_tutor(self):
        tutor = Tutor( first_name ="Hayford", last_name="Ansah",  email="o.ansah.hayford@gmail.com")
        tutor.save()

        c = Client()
        response = c.delete('/tutor/'+ str( tutor.id) )
        # print( response.content)
        self.assertEqual(response.status_code, 204)

    def test_assign_student_to_tutor(self):
        tutor = Tutor( first_name ="Kofi", last_name="Mensah",  email="o.ansah.hayford@gmail.com")
        tutor.save()
        student = Student( first_name ="Hayford", last_name="Ansah", department="Computer science",  email="student@gmail.com")
        student.save()
        c = Client()

        response = c.post('/student-tuttor/assign/',
        {
            "tutor_id" : tutor.id,
            "student_id": student.id
        } ,
        content_type='application/json')
        # print( response.content)
        self.assertEqual(response.status_code, 200)
        

class StudentTestCase(TestCase):
    def test_get_students(self):
        c = Client()
        response = c.get('/students/')
        self.assertEqual(response.status_code, 200)
        
    def test_get_student(self):
        student = Student( first_name ="Hayford", last_name="Ansah", department="COmputer science",  email="o.ansah.hayford@gmail.com")
        student.save()

        c = Client()
        response = c.get('/student/'+ str(student.id))
        self.assertEqual(response.status_code, 200)
        
    def test_create_student(self):
        
        c = Client()
        response = c.post('/students/' ,
        {
            "first_name": "hayford2",
            "last_name" : "ansah2",
            "department": "I.T",
            "email":"hayford2@gamil.com"

        })
        self.assertEqual(response.status_code, 201)
        
    def test_edit_student(self):
        student = Student( first_name ="Hayford", last_name="Ansah", department="I.T",  email="o.ansah.hayford@gmail.com")
        student.save()

        c = Client()
        response = c.put('/student/'+ str( student.id) ,
        {
            "first_name": "hayfordEdited",
            "last_name" : "ansahEdited",
            "department" : "Computer science",
            "email":"hayford@gamil.com"

        },
        content_type='application/json')
        # print( response.content)
        self.assertEqual(response.status_code, 201)
        
    def test_delete_student(self):
        student = Student( first_name ="Hayford", last_name="Ansah",  email="o.ansah.hayford@gmail.com")
        student.save()

        c = Client()
        response = c.delete('/student/'+ str( student.id) )
        # print( response.content)
        self.assertEqual(response.status_code, 204)
