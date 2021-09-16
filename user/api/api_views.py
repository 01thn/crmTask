from rest_framework import viewsets

from ..models import UserModel
from ..api.serializers import UserModelSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = UserModel.objects.all()