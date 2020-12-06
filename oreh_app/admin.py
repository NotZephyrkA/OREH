from django.contrib import admin

# Register your models here.
from oreh_app.models import Graduate, Resident, NatPer, Workers, \
    LegalEntity, BusinessModel, FinancialPlan, Team, Person, Courses, Participant, Project,  Services, FieldOfActivity, Achievements, Competitors

admin.site.register(FieldOfActivity)
admin.site.register(Person)
admin.site.register(Participant)
admin.site.register(Courses)
admin.site.register(Team)
admin.site.register(Graduate)
admin.site.register(Resident)
admin.site.register(NatPer)
admin.site.register(Workers)
admin.site.register(LegalEntity)
admin.site.register(BusinessModel)
admin.site.register(FinancialPlan)
admin.site.register(Project)
admin.site.register(Services)
admin.site.register(Achievements)
admin.site.register(Competitors)

