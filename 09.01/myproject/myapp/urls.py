from django.urls import path
from . import views

urlpatterns = [
    path('students/<int:course_id>/', views.get_students_of_course, name='get_students_of_course'),
]