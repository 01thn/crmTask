from rest_framework import viewsets

from ..models import Person
from ..api.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()