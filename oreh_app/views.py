from django.shortcuts import render
from django.views.generic.base import View

from oreh_app.models import Achievement, Services, Questions, Resident, Project


class IndexView(View):
    def get(self, request):
        achievements = Achievement.objects.all().order_by('date')[:10]
        services = Services.objects.all()
        questions = Questions.objects.all()
        return render(request, 'index.html',
                      {'achievements': achievements, 'services': services, 'questions': questions})


class ResidentsView(View):
    def get(self, request):
        residents = Resident.objects.all()
        return render(request, 'residents.html', {'residents': residents})


class CurrentProjectsView(View):
    def get(self, request):
        current_projects = Project.objects.all()
        return render(request, 'current projects.html', {'current_projects': current_projects})


class ProjectView(View):
    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        return render(request, 'project.html', {'project': project})


class ResidentView(View):
    def get(self, request, resident_id):
        resident = Resident.objects.get(id=resident_id)
        return render(request, 'resident.html', {'resident': resident})


class AchievementView(View):
    def get(self, request):
        achievements = Achievement.objects.all()
        return render(request, 'achievements.html', {'achievements': achievements})
