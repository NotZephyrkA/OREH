from django.db import models


class BusinessModel(models.Model):
    earnings = models.TextField("Зароботок")
    distribution = models.TextField("Дистрибуция")
    promotionStrategy = models.TextField("Стратегия продвижения")

    def __str__(self):
        return self.earnings

    class Meta:
        verbose_name = "Бизнес модель"
        verbose_name_plural = "Бизнес модели"


class FinancialPlan(models.Model):
    projectCosts = models.TextField("Расходы по проекту")
    expectedResults = models.TextField(" Ожидаемые ключевые финансовые результаты")
    requestedFunds = models.TextField("Запрашиваемый объем денежных средств ")

    def __str__(self):
        return self.expectedResults

    class Meta:
        verbose_name = "Финансовый план"
        verbose_name_plural = "Финансовые планы"


class Participant(models.Model):
    pass


class FieldOfActivity(models.Model):
    pass


class Team(models.Model):
    name = models.CharField("Имя", max_length=100)
    # fieldOfActivity = models.ForeignKey(FieldOfActivity, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Сфера деятельности")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"


class Activity(models.Model):
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="Activity/")
    numberOfSeats = models.IntegerField("Кол-во мест")
    organizers = models.TextField("Организаторы")
    date = models.DateField("дата")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


# class Project(models.Model):
#     pass
#
#
# class FieldOfActivity(models.Model):
#     pass


class Person(models.Model):
    name = models.CharField("Имя", max_length=100)
    # project = models.ManyToManyField(Project, verbose_name="Проект")
    # fieldOfActivity = models.ForeignKey(FieldOfActivity, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Сфера деятельности")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Лицо"
        verbose_name_plural = "Лица"


class Courses(models.Model):
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    dateOfStart = models.DateField("Дата начала")
    dateOfCompletion = models.DateField("Дата завершения")
    author = models.TextField("Автор")
    numberOfSeats = models.TextField("Кол-во мест")
    placeToHost = models.TextField("Место проведения")
    sphere = models.TextField("Сфера")
    requirementsForACandidate = models.TextField("Требования к кандидату")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курсы"
        verbose_name_plural = "Курсы"


class Participant(models.Model):
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="команда")
    image = models.ImageField("Изображение", upload_to="Participant/")
    person = models.OneToOneField(Person, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Лицо")
    # activity = models.ManyToManyField(Activity, verbose_name="мероприятие")
    # courses = models.ManyToManyField(Courses, verbose_name="Курсы")

    def __str__(self):
        return self.person.__str__()

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"


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


class FieldOfActivity(models.Model):
    name = models.CharField("Имя", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сфера деятельности"
        verbose_name_plural = "Сферы деятельности"


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
