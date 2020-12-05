from django.db import models


# Сфера деятельности
class FieldOfActivity(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


# Лицо
class Person(models.Model):
    field_of_activity = models.ForeignKey(FieldOfActivity, null=True, blank=True, on_delete=models.SET_NULL)


# Курсы
class Courses(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    date_of_start = models.DateField()
    date_of_end = models.DateField()
    author = models.CharField(max_length=128)
    count_place = models.IntegerField()
    place = models.TextField()
    requirement = models.TextField()
    field_of_activity = models.ForeignKey(FieldOfActivity, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


# Участник
class Participant(models.Model):
    photo = models.ImageField()
    description = models.TextField()
    per = models.OneToOneField(Person, on_delete=models.CASCADE)
    team = models.ForeignKey(FieldOfActivity, null=True, blank=True, on_delete=models.SET_NULL)
    courses = models.ManyToManyField(Courses, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.description


# Команда
class Team(models.Model):
    participant = models.ManyToManyField(Participant)
    title = models.CharField(max_length=128)
    field_of_activity = models.ForeignKey(FieldOfActivity, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


# Выпускник
class Graduate(models.Model):
    photo = models.ImageField()
    description = models.TextField()
    team = models.ForeignKey(FieldOfActivity, null=True, blank=True, on_delete=models.SET_NULL)
    per = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.per


# Резидент
class Resident(models.Model):
    name = models.CharField(max_length=128)
    second_name = models.CharField(max_length=128)
    team = models.ForeignKey(FieldOfActivity, null=True, blank=True, on_delete=models.SET_NULL)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.second_name}"


# Физическое лицо
class NatPer(models.Model):
    name = models.CharField(max_length=128)
    second_name = models.CharField(max_length=128)
    # Отчество
    middle_name = models.CharField(max_length=128)
    team = models.ForeignKey(FieldOfActivity, null=True, blank=True, on_delete=models.SET_NULL)
    per = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.second_name}"


# Работники
class Workers(models.Model):
    nat_per = models.OneToOneField(NatPer, on_delete=models.CASCADE)

    def __str__(self):
        return self.nat_per.name


# Юр. Лицо
class LegalEntity(models.Model):
    per = models.OneToOneField(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    team = models.ForeignKey(FieldOfActivity, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
