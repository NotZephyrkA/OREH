from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.base import View

from oreh_app.models import Achievement, Services, Questions, Resident, Project, Profile


class IndexView(View):
    def get(self, request):
        achievements = Achievement.objects.all().order_by('date')[:10]
        services = Services.objects.all()
        questions = Questions.objects.all()
        return render(request, 'oreh_app/index.html',
                      {'achievements': achievements, 'services': services, 'questions': questions})


class ResidentsView(View):
    def get(self, request):
        residents = Resident.objects.all()
        return render(request, 'oreh_app/residents.html', {'residents': residents})


class CurrentProjectsView(View):
    def get(self, request):
        current_projects = Project.objects.all()
        return render(request, 'oreh_app/current projects.html', {'current_projects': current_projects})


class ProjectView(View):
    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        return render(request, 'oreh_app/project.html', {'project': project})


class ResidentView(View):
    def get(self, request, resident_id):
        resident = Resident.objects.get(id=resident_id)
        return render(request, 'oreh_app/resident.html', {'resident': resident})


class AchievementView(View):
    def get(self, request):
        achievements = Achievement.objects.all()
        return render(request, 'oreh_app/achievements.html', {'achievements': achievements})



class PersonalAccount(View):
    @login_required
    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        resident = profile.resident
        context = {}
        if resident is not None:
            project = resident.project.get()
            context['project'] = project
        else:
            context['project'] = None

        return render(request, 'oreh_app/personal-account.html', context)
