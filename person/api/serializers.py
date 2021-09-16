from rest_framework import serializers

from ..models import Person


class PersonSerializer(serializers.ModelSerializer):
    lastName = serializers.CharField(required=True)
    firstName = serializers.CharField(required=True)
    patronymic = serializers.CharField(required=True)
    age = serializers.CharField(required=True)
    is_active = serializers.BooleanField(required=True)
    education = serializers.CharField(required=True)
    company = serializers.StringRelatedField(many=True)
    position = serializers.CharField(required=True)
    skills = serializers.StringRelatedField(many=True)
    created_at = serializers.DateTimeField(required=True)
    updated_at = serializers.DateTimeField(required=True)

    class Meta:
        model = Person
        fields = '__all__'