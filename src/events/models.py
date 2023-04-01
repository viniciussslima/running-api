from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    distance = models.IntegerField()
    pace = models.TimeField()
    overall_position = models.IntegerField()
    age_position = models.IntegerField()
    age_category = models.CharField(max_length=10)
    certificate = models.OneToOneField(
        "Asset",
        related_name="certificate",
        on_delete=models.PROTECT,
        null=True,
    )
    photos = models.ManyToManyField("Asset", related_name="photos", blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.name


class Asset(models.Model):
    url = models.FileField(upload_to="assets/")

    def __str__(self):
        return f"Asset: {self.url}"
