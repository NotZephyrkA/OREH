from django.db import models


# Сфера деятельности
class FieldOfActivity(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


# Лицо
class Person(models.Model):
    name = models.CharField("Имя", max_length=100)
    field_of_activity = models.ForeignKey(FieldOfActivity, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Лицо"
        verbose_name_plural = "Лица"


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


class FinancialPlan(models.Model):
    projectCosts = models.TextField("Расходы по проекту")
    expectedResults = models.TextField(" Ожидаемые ключевые финансовые результаты")
    requestedFunds = models.TextField("Запрашиваемый объем денежных средств ")

    def __str__(self):
        return self.expectedResults

    class Meta:
        verbose_name = "Финансовый план"
        verbose_name_plural = "Финансовые планы"


class BusinessModel(models.Model):
    earnings = models.TextField("Зароботок")
    distribution = models.TextField("Дистрибуция")
    promotionStrategy = models.TextField("Стратегия продвижения")

    def __str__(self):
        return self.earnings

    class Meta:
        verbose_name = "Бизнес модель"
        verbose_name_plural = "Бизнес модели"


class Project(models.Model):
    name = models.CharField("Имя", max_length=100)
    descriptionOfTheProblem = models.TextField("Описание проблемы")
    solutionToTheProblem = models.TextField("Решение проблемы")
    solutionBenefits = models.TextField("Приемущества решения")
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Команда")
    dateOfStart = models.DateField("Дата начала")
    dateOfCompletion = models.DateField("Дата завершения")
    financialPlan = models.OneToOneField(FinancialPlan, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Финансовый план")
    businessModel = models.OneToOneField(BusinessModel, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Бизнес модель")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Services(models.Model):
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"


class Achievements(models.Model):
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Лицо")
    date = models.TextField("Дата")
    description = models.TextField("Описание")
    name = models.CharField("Имя", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"


class Competitors(models.Model):
    project = models.OneToOneField(Project, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Проект")
    name = models.CharField("Имя", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Конкурент"
        verbose_name_plural = "Конкуренты"
