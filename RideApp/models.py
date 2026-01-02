from django.db import models
from AuthApp.models import User

# Create your models here.
class Ride(models.Model):
    rider = models.ForeignKey(
        User,
        related_name='rider_rides',
        on_delete=models.CASCADE
    )
    driver = models.ForeignKey(
        User,
        related_name='driver_rides',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    pickup_location = models.CharField(max_length=255)
    drop_off_location = models.CharField(max_length=255)
    current_location = models.CharField(max_length=255, blank=True, null=True)

    STATUS_CHOICES = (
        ('requested', 'Requested'),
        ('accepted', 'Accepted'),
        ('started', 'Started'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='requested'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)