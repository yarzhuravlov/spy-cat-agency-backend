from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.mixins import BaseViewSetMixin
from missions.models import Mission, Target
from missions.permissions import DeleteIfIsUnassigned, IsCatAssignedToMission
from missions.serializers import (
    MissionSerializer,
    TargetSerializer,
    NoteSerializer,
    MissionRetrieveSerializer,
    TargetRetrieveSerializer,
)


class MissionViewSet(BaseViewSetMixin, viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = [IsAuthenticated, DeleteIfIsUnassigned]

    action_serializers = {
        "retrieve": MissionRetrieveSerializer,
    }


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

    @action(detail=True, methods=["GET"], url_path="complete")
    def complete(self, *args, **kwargs):
        target = self.get_object()
        target.is_completed = True
        target.save()
        return Response(TargetRetrieveSerializer(instance=target).data)

    @action(detail=True, methods=["POST"], url_path="note")
    def add_note(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(
            data={
                "text": request.data["text"],
            }
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(target=self.get_object())

        return Response(serializer.data, status.HTTP_201_CREATED)
