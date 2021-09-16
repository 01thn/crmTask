from rest_framework.generics import ListAPIView

from .serializers import CompaniesSerializer
from ..models import Companies


class CompaniesListAPIView(ListAPIView):

    serializer_class = CompaniesSerializer
    queryset = Companies.objects.all()