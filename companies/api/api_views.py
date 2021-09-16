from rest_framework import viewsets

from ..models import Companies
from ..api.serializers import CompaniesSerializer


class CompaniesViewSet(viewsets.ModelViewSet):
    serializer_class = CompaniesSerializer
    queryset = Companies.objects.all()