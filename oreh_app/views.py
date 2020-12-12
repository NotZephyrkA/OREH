from django.shortcuts import render
from django.views.generic.base import View

from oreh_app.models import Resident


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class ResidentsView(View):
    def get(self, request):
        residents = Resident.objects.all()
        return render(request, 'residents.html', {'residents': residents})
