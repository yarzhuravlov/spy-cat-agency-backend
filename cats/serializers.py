from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from cats.models import Cat
from cats.services import CatService, BreedService

breed_service = BreedService()


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ["name", "years_of_experience", "breed", "salary"]

    def validate_breed(self, value):
        return breed_service.validate(value, ValidationError)

    def validate_name(self, value):
        Cat.validate_name(value, ValidationError)
        return value

    def create(self, validated_data):
        return CatService.create(**validated_data)
