from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=63, unique=True)
    years_of_experience = models.PositiveIntegerField()
    breed = models.CharField(max_length=63)
    salary = models.PositiveIntegerField()
