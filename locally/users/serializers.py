from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)