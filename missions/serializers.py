from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from cats.models import Cat
from missions.models import Mission, Target, Note


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ["id", "mission", "name", "country", "is_completed"]


class TargetCreateSerializer(TargetSerializer):
    class Meta(TargetSerializer.Meta):
        fields = ["name", "country"]


class MissionSerializer(serializers.ModelSerializer):
    cat = serializers.PrimaryKeyRelatedField(
        queryset=Cat.objects.all(),
        required=False,
        allow_null=True,
    )
    targets = TargetCreateSerializer(many=True)

    class Meta:
        model = Mission
        fields = ["id", "cat", "targets"]

    def validate_targets(self, value):
        if not 1 <= len(value) <= 3:
            raise ValidationError(
                {"targets": "A mission must have between 1 and 3 targets."}
            )
        return value

    def create(self, validated_data):
        targets_data = validated_data.pop("targets")

        with transaction.atomic():
            mission = Mission.objects.create(**validated_data)
            for target_data in targets_data:
                Target.objects.create(**target_data, mission=mission)

        return mission


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["target", "text", "created_at"]
        read_only_fields = ["target", "created_at"]


class TargetRetrieveSerializer(TargetSerializer):
    notes = NoteSerializer(many=True)

    class Meta(TargetSerializer.Meta):
        fields = ["id", "name", "country", "is_completed", "notes"]


class MissionRetrieveSerializer(MissionSerializer):
    targets = TargetRetrieveSerializer(many=True)
