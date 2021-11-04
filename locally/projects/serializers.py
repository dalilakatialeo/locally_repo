from re import S
from rest_framework import serializers
from .models import SUB_CHOICES, Project, Donation

class DonationSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    # type = serializers.CharField(max_length=1)
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    donor = serializers.CharField(max_length=200)
    project_id = serializers.IntegerField()

    #this will be called for POST / donations to create a new donation
    def create(self, validated_data):
        return Donation.objects.create(**validated_data)


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    location = serializers.ChoiceField(choices=SUB_CHOICES)
    goal = serializers.IntegerField()
    # donation_type = serializers.ChoiceField(choices = Project.DONATION)
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    # goal = serializers.ReadOnlyField()
    date_created = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner.id')
    # donations = DonationSerializer(many=True, read_only=True)

#this will be called to POST /projects to create a new project
    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    #many=True tells the nested serializer to include a list of items
    #read_ony = True means its only used for GET, not PUT (which means you cant provide donations when you are updating a project)
    donations = DonationSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.location = validated_data.get('location', instance.location)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        # instance.goal = validated_data.get('goal', instance.goal)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance. save()
        return instance
        
class DonationDetailSerializer(DonationSerializer):
    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount',instance.amount)
        instance.comment = validated_data.get('comment',instance.comment)
        instance.anonymous = validated_data.get ('anonymous', instance.anonymous)
        instance.project_id = validated_data.get ('project_id', instance.project_id)
        instance.save()
        return instance
