from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from missions.models import Mission
from missions.permissions import DeleteIfIsUnassigned
from missions.serializers import MissionSerializer


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = [IsAuthenticated, DeleteIfIsUnassigned]
