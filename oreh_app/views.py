from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.base import View

from oreh_app.models import Achievement, Services, Questions, Resident, Project, Profile, Graduate, Courses, Event
from .templates.oreh_app.recomendation import getRecommendations, transformPrefs


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
    def get(self, request):
        courses = Courses.objects.all()
        marks_courses = {}
        for course in courses:
            marks = course.mark_set.all()
            marks_map = {}
            for mark in marks:
                marks_map[mark.user] = mark.mark
            marks_courses[course] = marks_map
        profile = Profile.objects.get(user=request.user)
        recommendations = getRecommendations(transformPrefs(marks_courses), profile.user)

        # Рекомендации

        return render(request, 'oreh_app/personal-account.html', {'recommendations': recommendations})


class GraduatesView(View):
    def get(self, request):
        graduates = Graduate.objects.all()
        return render(request, 'oreh_app/graduates.html', {'graduates': graduates})


class CoursesView(View):
    def get(self, request):
        courses = Courses.objects.all()
        return render(request, 'oreh_app/courses.html', {'courses': courses})


class CourseView(View):
    def get(self, request, course_id):
        course = Courses.objects.get(id=course_id)
        return render(request, 'oreh_app/course.html', {'course': course})


class EventsView(View):
    def get(self, request):
        events = Event.objects.all()
        return render(request, 'oreh_app/events.html', {'events': events})


class EventView(View):
    def get(self, request, event_id):
        event = Event.objects.get(id=event_id)
        return render(request, 'oreh_app/event.html', {'event': event})


from datetime import datetime, date
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar


class CalendarView(generic.ListView):
    model = Event
    template_name = 'oreh_app/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()
