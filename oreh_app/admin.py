from django.contrib import admin

# Register your models here.
from oreh_app.models import FieldOfActivity, Person, Participant, Courses, Team, Graduate, Resident, NatPer, Workers, \
    LegalEntity

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
