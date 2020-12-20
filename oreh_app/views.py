from django.shortcuts import render
from django.views.generic.base import View

from oreh_app.models import Achievement, Services, Questions


class IndexView(View):
    def get(self, request, achievement_id):
        achievements = Achievement.objects.all().order_by('date')[:10]
        services = Services.objects.all()
        questions = Questions.objects.all()
        achievements = Achievement.objects.all(id=achievement_id)
        return render(request, 'index.html',
                      {'achievements': achievements, 'services': services, 'questions': questions})
