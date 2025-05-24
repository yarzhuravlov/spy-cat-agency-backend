from django.core.exceptions import ValidationError
from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=63, unique=True)
    years_of_experience = models.PositiveIntegerField()
    breed = models.CharField(max_length=63)
    salary = models.PositiveIntegerField()

    @staticmethod
    def validate_name(name: str, error_to_raise: type[Exception]):
        if Cat.objects.filter(name__iexact=name):
            raise error_to_raise(
                {"name": "Cat with this Name already exists."},
            )

    def clean(self):
        Cat.validate_name(self.name, ValidationError)

    def save(
        self,
        *,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        self.full_clean()
        return super().save(force_insert, force_update, using, update_fields)
