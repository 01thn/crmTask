from rest_framework.generics import ListAPIView

from .serializers import UserSerializer
from ..models import UserModel


class UserListAPIView(ListAPIView):

    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
