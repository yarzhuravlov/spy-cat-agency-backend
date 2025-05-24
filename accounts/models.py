from django.contrib.auth.models import AbstractUser
from django.db import models

from cats.models import Cat


class User(AbstractUser):
    agent = models.ForeignKey(Cat, null=True, on_delete=models.CASCADE)
