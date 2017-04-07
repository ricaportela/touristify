"""Tour points registration."""
from django.db import models


class Tourpoint(models.Model):
    """Tour points registration."""
    name = models.CharField(max_length=100, blank=True, default='')
    latitude = models.DecimalField(max_digits=8, decimal_places=3)
    longitude = models.DecimalField(max_digits=8, decimal_places=3)
    category = models.CharField(max_length=30, blank=True, default='')
    point_type = models.CharField(max_length=8, blank=True, default='') # public or provate register

    class Meta:
        ordering = ('name',)
