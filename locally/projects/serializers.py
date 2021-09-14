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

class ProjectDetailSerializer(ProjectSerializer):
    donations = DonationSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.location = validated_data.get('location', instance.location)
        instance.donation = validated_data.get('donation', instance.donation)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        return instance
        