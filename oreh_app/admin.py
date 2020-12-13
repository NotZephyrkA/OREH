from django.contrib import admin

# Register your models here.
from oreh_app.models import FieldOfActivity, Profile, Event, Courses, Achievement, Graduate, Resident, Project, \
    Participant, Position, BusinessModel, FinancialPlan

admin.site.register(FieldOfActivity)
admin.site.register(FinancialPlan)
admin.site.register(BusinessModel)
admin.site.register(Position)
admin.site.register(Participant)
admin.site.register(Project)
admin.site.register(Resident)
admin.site.register(Graduate)
admin.site.register(Achievement)
admin.site.register(Courses)
admin.site.register(Event)
admin.site.register(Profile)

