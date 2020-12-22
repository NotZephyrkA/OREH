from django.shortcuts import render
from django.views.generic.base import View

from oreh_app.models import Graduate


class IndexView(View):
    def get(self,request):
        return render(request, 'index.html')


class GraduatesView(View):
    def get(self, request):
        graduates = Graduate.objects.all()
        return render(request, 'graduates.html', {'graduates': graduates})


class CoursesView(View):
    def get(self, request, project_id):
        course = Course.object.get(id=project_id)
        return render(request, 'courses.html', {'course': course})