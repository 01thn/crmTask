from rest_framework import serializers

from ..models import Companies


class CompaniesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    is_active = serializers.BooleanField(required=True)
    location = serializers.CharField(required=True)
    numOffices = serializers.CharField(required=True)
    connection = serializers.StringRelatedField(many=True)
    created_at = serializers.DateTimeField(required=True)
    updated_at = serializers.DateTimeField(required=True)

    class Meta:
        model = Companies
        fields = '__all__'