from rest_framework import viewsets

from ..models import Skills
from ..api.serializers import SkillsSerializer


class SkillsViewSet(viewsets.ModelViewSet):
    serializer_class = SkillsSerializer
    queryset = Skills.objects.all()