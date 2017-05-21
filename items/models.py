from django.db import models
from django.urls import reverse


class Location(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('items:location-detail', kwargs={'pk':self.pk})


class Task(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    location = models.ForeignKey(Location, related_name='tasks') # default = task_set
    title = models.CharField(max_length=32)
    body = models.CharField(max_length=1024, blank=True, default="", null=False)

    def __str__(self):
        return self.title + self.location.name

