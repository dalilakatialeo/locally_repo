from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.TextField()
    donation = models.TextField()
    # DONATION = (
    #     ('M', 'Money'),
    #     ('T', 'Time'),
    #     ('S', 'Skill'),
    #     ('R', 'Resources'),
    # )
    # donation_type = models.CharField(max_length=1, choices=DONATION)    
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )

class Donation(models.Model):
    type = models.CharField(max_length=1)
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='donations'
    )
    donor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='donor_donations'
    )
