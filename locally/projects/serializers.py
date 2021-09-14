from re import S
from rest_framework import serializers
from .models import Project, Donation

class DonationSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    type = serializers.CharField(max_length=1)
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    donor = serializers.CharField(max_length=200)
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Donation.objects.create(**validated_data)


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    location = serializers.CharField(max_length=None)
    donation = serializers.CharField(max_length=None)
    # donation_type = serializers.ChoiceField(choices = Project.DONATION)
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner.id')
    # donations = DonationSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

