from django.shortcuts import render
from django.views.generic.base import View

from oreh_app.models import Resident, Project


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class ResidentsView(View):
    def get(self, request):
        residents = Resident.objects.all()
        return render(request, 'residents.html', {'residents': residents})


class CurrentProjectsView(View):
    def get(self, request):
        current_projects = Project.objects.all()
        return render(request, 'current projects.html', {'current projects': current_projects})
