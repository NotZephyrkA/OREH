from django.db import models
class Team(models.Model):
    Participant = models.ManyToManyField(list)
    title = models.CharField(maxlength=128)