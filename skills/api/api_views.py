from rest_framework.generics import ListAPIView

from .serializers import SkillsSerializer
from ..models import Skills


class SkillsListAPIView(ListAPIView):

    serializer_class = SkillsSerializer
    queryset = Skills.objects.all()