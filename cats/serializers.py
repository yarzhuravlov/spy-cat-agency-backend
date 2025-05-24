from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from cats.models import Cat
from cats.services import CatService, BreedService

breed_service = BreedService()


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ["id", "name", "years_of_experience", "breed", "salary"]

    def validate_breed(self, value):
        return breed_service.validate(
            value, ValidationError, "Breed is invalid."
        )

    def validate_name(self, value):
        Cat.validate_name(value, ValidationError, raising_payload="Cat with this Name already exists.")
        return value

    def create(self, validated_data):
        return CatService.create(**validated_data)


class CatUpdateSerializer(CatSerializer):
    class Meta(CatSerializer.Meta):
        read_only_fields = ["name", "years_of_experience", "breed"]
