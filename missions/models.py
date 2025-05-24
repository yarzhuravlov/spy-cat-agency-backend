from django.db import models

from cats.models import Cat


class Mission(models.Model):
    cat = models.ForeignKey(
        Cat,
        on_delete=models.CASCADE,
        related_name="missions",
    )


class Target(models.Model):
    mission = models.ForeignKey(
        Mission,
        on_delete=models.CASCADE,
        related_name="targets",
    )
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=63)
    is_completed = models.BooleanField(default=False)


class Note(models.Model):
    target = models.ForeignKey(
        Target,
        on_delete=models.CASCADE,
        related_name="notes",
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
