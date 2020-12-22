from django.shortcuts import render
from django.views.generic.base import View

from oreh_app.models import Graduate, Courses


class IndexView(View):
    def get(self,request):
        return render(request, 'index.html')


class GraduatesView(View):
    def get(self, request):
        graduates = Graduate.objects.all()
        return render(request, 'graduates.html', {'graduates': graduates})


class CoursesView(View):
    def all(self, request, course_id):
        course = Courses.object.get(id=course_id)
        return render(request, 'courses.html', {'course': course})


class CourseView(View):
    def get(self, request,):
        course = Courses.object.all()
        return render(request, 'courses.html', {'course': course})