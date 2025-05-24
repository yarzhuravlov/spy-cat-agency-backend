from django.contrib.auth import get_user_model
from django.db import transaction

from cats.models import Cat

User = get_user_model()


class CatService:
    @staticmethod
    def create(**validated_data) -> Cat:
        with transaction.atomic():
            cat = Cat.objects.create(**validated_data)
            User.objects.create_user(
                username=validated_data["name"].lower(),
                agent=cat,
            )

            return cat
