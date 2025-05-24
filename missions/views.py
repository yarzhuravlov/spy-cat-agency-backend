from rest_framework import viewsets

from missions.models import Mission
from missions.serializers import MissionSerializer


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
