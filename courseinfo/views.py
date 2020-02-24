from django.shortcuts import render, get_object_or_404, render_to_response
from django.http.response import HttpResponse
from django.template import loader
from django.views import View

from .models import (Instructor, Student, Section, Semester, Course, Registration)


# Create your views here.
# def instructor_list_view(request):
#     instructor_list = Instructor.objects.all()
#     template = loader.get_template('courseinfo/instructor_list.html')
#     context = {'instructor_list':instructor_list}
#     output = template.render(context)
#     return HttpResponse(output)

class InstructorList(View):
    def get(self,request):
        return render(
            request,
            'courseinfo/instructor_list.html',
            {'instructor_list':Instructor.objects.all()}
        )


class InstructorDetail(View):
    def get(self, request, pk):
        instructor = get_object_or_404(
            Instructor, pk=pk
        )
        section_list = instructor.sections.all()
        return render_to_response(
            'courseinfo/instructor_detail.html',
            {'instructor':instructor,'section_list':section_list}
        )


class StudentList(View):

    def get(self,request):
        return render(
            request,
            'courseinfo/student_list.html',
            {'student_list':Student.objects.all()}
        )

class StudentDetail(View):
    def get(self, request, pk):
        student = get_object_or_404(
            Student, pk=pk
        )
        registration_list = student.registrations.all()
        return render_to_response(
            'courseinfo/student_detail.html',
            {'student':student,'registration_list':registration_list}
        )




class SectionList(View):

    def get(self,request):
        return render(
            request,
            'courseinfo/section_list.html',
            {'section_list':Section.objects.all()}
        )

class SectionDetail(View):
    def get(self, request, pk):
        section = get_object_or_404(
            Section, pk=pk
        )
        semester = section.semester
        course = section.course
        instructor = section.instructor
        registration_list = section.registrations.all()
        section_list = instructor.sections.all()
        return render_to_response(
            'courseinfo/section_detail.html',
            {'instructor':instructor,
             'section':section,
             'semester':semester,
             'course':course,
             'registration_list':registration_list}
        )


class SemesterList(View):

    def get(self,request):
        return render(
            request,
            'courseinfo/semester_list.html',
            {'semester_list':Semester.objects.all()}
        )

class SemesterDetail(View):
    def get(self, request, pk):
        semester = get_object_or_404(
            Semester, pk=pk
        )
        section_list = semester.sections.all()
        return render_to_response(
            'courseinfo/semester_detail.html',
            {'semester':semester,'section_list':section_list}
        )


class RegistrationList(View):

    def get(self,request):
        return render(
            request,
            'courseinfo/registration_list.html',
            {'registration_list':Registration.objects.all()}
        )

class RegistrationDetail(View):
    def get(self, request, pk):
        registration = get_object_or_404(
            Registration, pk=pk
        )
        return render_to_response(
            'courseinfo/registration_detail.html',
            {'registration':registration}
        )



class CourseList(View):

    def get(self,request):
        return render(
            request,
            'courseinfo/course_list.html',
            {'course_list':Course.objects.all()}
        )

class CourseDetail(View):
    def get(self, request, pk):
        course = get_object_or_404(
            Course, pk=pk
        )
        section_list = course.sections.all()
        return render_to_response(
            'courseinfo/course_detail.html',
            {'course':course,'section_list':section_list}
        )

# old code
# def student_list_view(request):
#     student_list = Student.objects.all()
#     template = loader.get_template('courseinfo/student_list.html')
#     context = {'student_list':student_list}
#     output = template.render(context)
#     return HttpResponse(output)
