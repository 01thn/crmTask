from rest_framework import serializers

from ..models import UserModel


class UserSerializer(serializers.ModelSerializer):
    login = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    admin = serializers.BooleanField(required=True)
    last_login = serializers.DateTimeField(required=True)

    class Meta:
        model = UserModel
        fields = '__all__'
