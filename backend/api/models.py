from django.db import models


class Direction(models.Model):
    name = models.CharField(max_length=125)
    slug = models.SlugField(unique=True)
    sort_num = models.IntegerField()

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=125)
    slug = models.SlugField(unique=True)
    directions = models.ManyToManyField(Direction)
    description = models.TextField()
    date_of_birth = models.DateField()
    experience = models.IntegerField()
    sort_num = models.IntegerField()

    def __str__(self):
        return self.name
