from uuid import uuid4

import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction

from cats.models import Cat

User = get_user_model()


class BreedService:
    def __init__(
        self,
        breed_list_url: str = settings.BREED_API_URL,
        breed_list_limit: int = settings.BREED_LIMIT_BY_REQUEST,
    ):
        self.breed_list_url = breed_list_url
        self.breed_list_limit = breed_list_limit

    @staticmethod
    def normalize_breed_name(breed_name: str):
        return breed_name.lower().strip()

    @staticmethod
    def find_breed(breed_name: str, breeds: list) -> str | bool:
        breed_name = BreedService.normalize_breed_name(breed_name)

        for breed in breeds:
            if (
                fetched_breed_name := BreedService.normalize_breed_name(
                    breed.get("name")
                )
            ) == breed_name:
                return fetched_breed_name

        return False

    def make_request(self, limit: int, page: int = settings.BREED_START_PAGE):
        response = requests.get(
            f"{self.breed_list_url}?limit={limit}&page={page}"
        )

        if response.status_code != 200:
            raise ValueError("Breed API send non 200 response")

        return response.json()

    def validate(
        self,
        breed_name: str,
        error_to_rise=type[Exception],
    ) -> str | None:
        page = settings.BREED_START_PAGE

        while breeds := self.make_request(self.breed_list_limit, page):
            if fetched_breed_name := BreedService.find_breed(
                breed_name, breeds
            ):
                return fetched_breed_name

            page += 1

        raise error_to_rise(
            {"breed": "Breed is invalid."},
        )


class CatService:
    @staticmethod
    def create(**validated_data) -> Cat:
        username = validated_data["name"].lower()
        password = uuid4()

        with transaction.atomic():
            cat = Cat.objects.create(**validated_data)
            User.objects.create_user(
                username=username,
                password=str(password),
                agent=cat,
            )

            print(
                f"Created User with username: {username} "
                f"& password {password}"
            )

            return cat
