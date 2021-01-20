from django.shortcuts import render
from django.views.generic.base import View

from oreh_app.models import Achievement, Services, Questions, Resident, Project, Graduate, Courses, Event


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

    def get(self, request):
        return render(request, 'index.html')


class GraduatesView(View):
    def get(self, request):
        graduates = Graduate.objects.all()
        return render(request, 'graduates.html', {'graduates': graduates})


class CoursesView(View):
    def get(self, request):
        courses = Courses.objects.all()
        return render(request, 'courses.html', {'courses': courses})


class CourseView(View):
    def get(self, request, course_id):
        course = Courses.objects.get(id=course_id)
        return render(request, 'course.html', {'course': course})


class EventsView(View):
    def get(self, request):
        events = Event.objects.all()
        return render(request, 'events.html', {'events': events})

    class EventView(View):
        def get(self, request, event_id):
            event = Event.objects.get(id=event_id)
            return render(request, 'event.html', {'event': event})


from datetime import datetime, date
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar


class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

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
