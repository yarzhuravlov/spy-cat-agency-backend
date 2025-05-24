from rest_framework import viewsets

from cats.models import Cat
from cats.serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
