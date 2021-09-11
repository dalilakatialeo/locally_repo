from django.db import models

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
    owner = models.CharField(max_length=200)

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
    donor = models.CharField(max_length=200)
