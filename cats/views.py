from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from base.mixins import BaseViewSetMixin
from cats.models import Cat
from cats.serializers import CatSerializer, CatUpdateSerializer


class CatViewSet(BaseViewSetMixin, viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]

    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    action_serializers = {
        "update": CatUpdateSerializer,
        "partial_update": CatUpdateSerializer,
    }
