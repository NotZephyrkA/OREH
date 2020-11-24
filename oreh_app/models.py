from django.db import models

# Create your models here.
class Activity(models.Model):
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="Activity/")
    location = models.TextField("место")
    organizer = models.ManyToManyField(Organizer, verbose_name="организатор")
    places = models.CharField("кол-во мест")
    date = models.TextField("дата")

