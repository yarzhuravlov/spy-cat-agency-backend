from django.db import transaction
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.mixins import BaseViewSetMixin
from missions.models import Mission, Target
from missions.permissions import (
    DeleteIfIsUnassigned,
    IsCatAssignedToMission,
    IsTaskNotCompleted,
)
from missions.serializers import (
    MissionSerializer,
    TargetSerializer,
    NoteSerializer,
    MissionRetrieveSerializer,
    TargetRetrieveSerializer,
    AssignCatToMissionSerializer,
)
from missions.services import MissionService


class MissionViewSet(
    BaseViewSetMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = [IsAuthenticated, DeleteIfIsUnassigned]

    action_serializers = {
        "retrieve": MissionRetrieveSerializer,
        "assign_cat": AssignCatToMissionSerializer,
    }

    @action(detail=True, methods=["POST"], url_path="assign")
    def assign_cat(self, request, *args, **kwargs):
        cat_missions = MissionService.get_cat_missions_for_update(request)

        with transaction.atomic():
            serializer = self.get_serializer_class()(
                instance=self.get_object(),
                data=request.data,
            )

            serializer.is_valid(raise_exception=True)

            MissionService.validate_cat_has_not_incomplete_mission(
                cat_missions,
                ValidationError,
            )

            serializer.save()

            return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        cat_missions = MissionService.get_cat_missions_for_update(request)
        with transaction.atomic():
            MissionService.validate_cat_has_not_incomplete_mission(
                cat_missions,
                ValidationError,
            )

            return super().create(request, *args, **kwargs)


class TargetViewSet(BaseViewSetMixin, viewsets.GenericViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminUser | IsCatAssignedToMission,
    ]

    action_serializers = {
        "add_note": NoteSerializer,
    }

    action_permissions = {
        "add_note": [
            IsAuthenticated,
            IsAdminUser | IsCatAssignedToMission,
            IsTaskNotCompleted,
        ]
    }

    @action(detail=True, methods=["GET"], url_path="complete")
    def complete(self, *args, **kwargs):
        target = self.get_object()
        target.is_completed = True
        target.save()
        return Response(TargetRetrieveSerializer(instance=target).data)

    @action(detail=True, methods=["POST"], url_path="note")
    def add_note(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(target=self.get_object())

        return Response(serializer.data, status.HTTP_201_CREATED)
