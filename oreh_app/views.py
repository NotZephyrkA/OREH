from django.shortcuts import render
from django.views.generic.base import View

from oreh_app.models import Achievement


class IndexView(View):
    def get(self, request):
        achievements = Achievement.objects.all()
        return render(request, 'index.html', {'achievements', achievements})