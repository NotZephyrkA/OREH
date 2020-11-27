from django.db import models


class BusinessModel(models.Model):
    earnings = models.TextField("Зароботок")
    distribution = models.TextField("Дистрибуция")
    promotionStrategy = models.TextField("Стратегия продвижения")

    class Meta:
        verbose_name = "Бизнес модель"
        verbose_name_plural = "Бизнес модели"


class FinancialPlan(models.Model):
    projectCosts = models.TextField("Расходы по проекту")
    expectedResults = models.TextField(" Ожидаемые ключевые финансовые результаты")
    requestedFunds = models.TextField("Запрашиваемый объем денежных средств ")

   class Meta:
        verbose_name = "Финансовый план"
        verbose_name_plural = "Финансовые планы"

class Participant:
    pass


class Team(models.Model):
    name = models.CharField("Имя", max_length=100)
    participant = models.ManyToManyField(Participant, verbose_name="Участник")

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"


class Activity(models.Model):
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="Activity/")
    numberOfSeats = models.TextField("Кол-во мест")
    organizers = models.TextField("Организаторы")
    places = models.CharField("кол-во мест")
    date = models.TextField("дата")

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


class Project:
    pass


class FieldOfActivity:
    pass


class Person(models.Model):
    project = models.ManyToManyField(Project, verbose_name="Проект")
    fieldOfActivity = models.ManyToManyField(FieldOfActivity, verbose_name="Сфера деятельности")

   class Meta:
        verbose_name = "Лицо"
        verbose_name_plural = "Лица"

class Courses(models.Model):
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    dateOfStart = models.TextField("Дата начала")
    dateOfCompletion = models.TextField("Дата завершения")
    author = models.TextField("Автор")
    numberOfSeats = models.TextField("Кол-во мест")
    placeToHost = models.TextField("Место проведения")
    sphere = models.TextField("Сфера")
    requirementsForACandidate = models.TextField("Требования к кандидату")

    class Meta:
        verbose_name = "Курсы"
        verbose_name_plural = "Курсы"


class Participant(models.Model):
    team = models.ManyToManyField(Team, verbose_name="команда")
    image = models.ImageField("Изображение", upload_to="Participant/")
    person = models.ManyToManyField(Person, verbose_name="Лицо")
    activity = models.ManyToManyField(Activity, verbose_name="мероприятие")
    courses = models.ManyToManyField(Courses, verbose_name="Курсы")

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"


class Project(models.Model):
    name = models.CharField("Имя", max_length=100)
    descriptionOfTheProblem = models.TextField("Описание проблемы")
    solutionToTheProblem = models.TextField("Решение проблемы")
    solutionBenefits = models.TextField("Приемущества решения")
    team = models.ManyToManyField(Team, verbose_name="Команда")
    dateOfStart = models.TextField("Дата начала")
    dateOfCompletion = models.TextField("Дата завершения")
    financialPlan = models.ManyToManyField(FinancialPlan, verbose_name="Финансовый план")
    businessModel = models.ManyToManyField(BusinessModel, verbose_name="Бизнес модель")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Services(models.Model):
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"


class FieldOfActivity(models.Model):
    name = models.CharField("Имя", max_length=100)

    class Meta:
        verbose_name = "Сфера деятельности"
        verbose_name_plural = "Сферы деятельности"


class Achievements(models.Model):
    person = models.ManyToManyField(Person, verbose_name="Лицо")
    date = models.TextField("Дата")
    description = models.TextField("Описание")
    name = models.CharField("Имя", max_length=100)

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"


class Competitors(models.Model):
    project = models.ManyToManyField(Project, verbose_name="Проект")
    name = models.CharField("Имя", max_length=100)

   class Meta:
        verbose_name = "Конкурент"
        verbose_name_plural = "Конкуренты"


