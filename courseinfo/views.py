from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader

from .models import (Instructor, Student, Section, Semester, Course, Registration)


# Create your views here.
def instructor_list_view(request):
    instructor_list = Instructor.objects.all()
    template = loader.get_template('courseinfo/instructor_list.html')
    context = {'instructor_list':instructor_list}
    output = template.render(context)
    return HttpResponse(output)

def student_list_view(request):
    student_list = Student.objects.all()
    template = loader.get_template('courseinfo/student_list.html')
    context = {'student_list':student_list}
    output = template.render(context)
    return HttpResponse(output)

def course_list_view(request):
    course_list = Course.objects.all()
    template = loader.get_template('courseinfo/course_list.html')
    context = {'course_list':course_list}
    output = template.render(context)
    return HttpResponse(output)

def section_list_view(request):
    section_list = Section.objects.all()
    template = loader.get_template('courseinfo/section_list.html')
    context = {'section_list':section_list}
    output = template.render(context)
    return HttpResponse(output)

def registration_list_view(request):
    registration_list = Registration.objects.all()
    template = loader.get_template('courseinfo/registration_list.html')
    context = {'registration_list':registration_list}
    output = template.render(context)
    return HttpResponse(output)

def semester_list_view(request):
    semester_list = Semester.objects.all()
    template = loader.get_template('courseinfo/semester_list.html')
    context = {'semester_list':semester_list}
    output = template.render(context)
    return HttpResponse(output)
