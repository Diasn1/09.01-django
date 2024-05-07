from django.shortcuts import render
from .models import Student, Course

def get_students_of_course(request, course_id):
    course = Course.objects.get(id=course_id)
    students = Student.objects.filter(course=course)
    return render(request, './myapp/students.html', {'students': students, 'course': course})