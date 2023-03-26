from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    pace = models.TimeField()
    overall_position = models.IntegerField()
    age_position = models.IntegerField()
    age_category = models.CharField(max_length=10)
    certificate = models.FileField(upload_to="certificates/")
    photos = models.ManyToManyField("Photo", blank=True)


class Photo(models.Model):
    image = models.ImageField(upload_to="event_photos/")
