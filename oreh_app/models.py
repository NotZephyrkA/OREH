from django.db import models


# Сфера деятельности
class FieldOfActivity(models.Model):
    name = models.CharField(maxlength=128)


# Лицо
class Person(models.Model):
    field_of_activity = models.ForeignKey(FieldOfActivity, on_delete=models.SET_NULL)


# Участник
class Participant(models.Model):
    photo = models.ImageField()
    description = models.TextField()


# Курсы
class Courses(models.Model):
    name = models.CharField(maxlength=128)
    description = models.TextField()
    date_of_start = models.DateField()
    date_of_end = models.DateField()
    author = models.CharField(maxlength=128)
    count_place = models.IntegerField()
    place = models.TextField()
    requirement = models.TextField()
    field_of_activity = models.ForeignKey(FieldOfActivity, on_delete=models.SET_NULL)


# Команда
class Team(models.Model):
    participant = models.ManyToManyField(Participant)
    title = models.CharField(maxlength=128)
    field_of_activity = models.ForeignKey(FieldOfActivity, on_delete=models.SET_NULL)


# Выпускник
class Graduate(models.Model):
    photo = models.ImageField()
    description = models.TextField()
    team = models.ForeignKey(FieldOfActivity, on_delete=models.SET_NULL)


# Резидент
class Resident(models.Model):
    name = models.CharField(maxlength=128)
    second_name = models.CharField(maxlength=128)
    team = models.ForeignKey(FieldOfActivity, on_delete=models.SET_NULL)
    person = models.OneToOneField(Person)


# Физическое лицо
class NatPer(models.Model):
    name = models.CharField(maxlength=128)
    second_name = models.CharField(maxlength=128)
    # Отчество
    middle_name = models.CharField(max_length=128)
    team = models.ForeignKey(FieldOfActivity, on_delete=models.SET_NULL)
    per = models.OneToOneField(Person)


# Работники
class Workers(models.Model):
    nat_per = models.OneToOneField(NatPer)


# Юр. Лицо
class LegalEntity(models.Model):
    per = models.OneToOneField(Person)
    title = models.CharField(maxlength=128)
    team = models.ForeignKey(FieldOfActivity, on_delete=models.SET_NULL)