from django.contrib.auth.models import User
from django.db import models


# Сфера деятельности
class FieldOfActivity(models.Model):
    name = models.CharField(max_length=128, default='name', verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сфера деятельности"
        verbose_name_plural = "Сферы деятельности"


# Финансовый план
class FinancialPlan(models.Model):
    projectCosts = models.TextField("Расходы по проекту")
    expectedResults = models.TextField(" Ожидаемые ключевые финансовые результаты")
    requestedFunds = models.TextField("Запрашиваемый объем денежных средств ")

    def __str__(self):
        return self.expectedResults

    class Meta:
        verbose_name = "Финансовый план"
        verbose_name_plural = "Финансовые планы"


# Бизнес модель
class BusinessModel(models.Model):
    earnings = models.TextField("Зароботок")
    distribution = models.TextField("Дистрибуция")
    promotionStrategy = models.TextField("Стратегия продвижения")

    def __str__(self):
        return self.earnings

    class Meta:
        verbose_name = "Бизнес модель"
        verbose_name_plural = "Бизнес модели"


# Должность
class Position(models.Model):
    name = models.CharField(max_length=128, default='name', verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"


# Участник
class Participant(models.Model):
    photo = models.ImageField(null=True, blank=True, verbose_name="Фото", upload_to="participant/", default='img_3.jpg')
    name = models.CharField(verbose_name='Имя', max_length=128, default='name')
    second_name = models.CharField(max_length=128, null=True, blank=True, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=128, null=True, blank=True, verbose_name="Отчество")
    place_of_study = models.TextField(null=True, blank=True, verbose_name="Место учебы")
    place_of_work = models.TextField(null=True, blank=True, verbose_name="Место работы")
    position = models.ForeignKey(Position, null=True, blank=True, on_delete=models.SET_NULL,
                                 verbose_name="Должность в проекте")

    @property
    def image_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return f"{self.name} {self.second_name}"

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"


# Проект
class Project(models.Model):
    photo = models.ImageField(null=True, blank=True, verbose_name="Фото", upload_to="resident/", default='img_3.jpg')
    name = models.CharField("Имя", max_length=100, default='name')
    fieldOfActivity = models.ForeignKey(FieldOfActivity, null=True, blank=True, on_delete=models.SET_NULL,
                                        verbose_name="Сфера деятельности")
    annotation = models.TextField(null=True, blank=True, verbose_name="Аннотация")
    descriptionOfTheProblem = models.TextField(null=True, blank=True, verbose_name="Описание проблемы")
    solutionToTheProblem = models.TextField(null=True, blank=True, verbose_name="Решение проблемы")
    solutionBenefits = models.TextField(null=True, blank=True, verbose_name="Приемущества решения")
    dateOfStart = models.DateField(null=True, blank=True, verbose_name="Дата начала")
    dateOfCompletion = models.DateField(null=True, blank=True, verbose_name="Дата завершения")
    financialPlan = models.OneToOneField(FinancialPlan, null=True, blank=True, on_delete=models.SET_NULL,
                                         verbose_name="Финансовый план")
    businessModel = models.OneToOneField(BusinessModel, null=True, blank=True, on_delete=models.SET_NULL,
                                         verbose_name="Бизнес модель")
    participants = models.ManyToManyField(Participant, blank=True,
                                          verbose_name="Участники")

    @property
    def image_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


# Резидент
class Resident(models.Model):
    photo = models.ImageField(null=True, blank=True, verbose_name="Фото", upload_to="resident/", default='img_3.jpg')
    name = models.CharField('Имя', max_length=128, default='name')
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Проект")

    @property
    def image_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Резидент"
        verbose_name_plural = "Резиденты"


# Выпускник
class Graduate(models.Model):
    resident = models.OneToOneField(Resident, on_delete=models.CASCADE, verbose_name="Резидент")

    def __str__(self):
        return self.resident.__str__()

    class Meta:
        verbose_name = "Выпускник"
        verbose_name_plural = "Выпускники"


# Достижение
class Achievement(models.Model):
    name = models.CharField("Имя", max_length=100, default='name')
    date = models.DateField("Дата")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    graduate = models.ForeignKey(Graduate, verbose_name="Выпускник", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"


# Курсы
class Courses(models.Model):
    photo = models.ImageField(null=True, blank=True, verbose_name="Фото", upload_to="curses/", default='img_3.jpg')
    name = models.CharField(max_length=128, default='name', verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    date_of_start = models.DateField("Дата начала")
    date_of_end = models.DateField("Дата окончания")
    author = models.CharField(max_length=128, null=True, blank=True, verbose_name="Автор")
    count_place = models.IntegerField("Количество мест")
    place = models.TextField("Место проведения")
    requirement = models.TextField(null=True, blank=True, verbose_name="Требования к кандидату")
    field_of_activity = models.ForeignKey(FieldOfActivity, null=True, blank=True, on_delete=models.SET_NULL,
                                          verbose_name="Сфера деятельноси")

    @property
    def image_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


# Мероприятие
class Event(models.Model):
    photo = models.ImageField(null=True, blank=True, verbose_name="Фото", upload_to="event/", default='img_3.jpg')
    name = models.CharField(max_length=128, default='name', verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    date_of_start = models.DateField("Дата начала")
    date_of_end = models.DateField("Дата окончания")
    author = models.CharField(max_length=128, null=True, blank=True, verbose_name="Организатор")
    count_place = models.IntegerField("Количество мест")
    place = models.TextField("Место проведения")

    @property
    def image_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


# Профиль
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    resident = models.OneToOneField(Resident, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Резидент")
    courses = models.ManyToManyField(Courses, blank=True, verbose_name="Курсы")
    events = models.ManyToManyField(Event, blank=True, verbose_name="Мероприятия")

    def __str__(self):
        return self.user.__str__()

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


# Услуги
class Services(models.Model):
    name = models.CharField(max_length=128, default='name', verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


# Вопрос
class Questions(models.Model):
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    answer = models.TextField(null=True, blank=True, verbose_name="Ответ")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"