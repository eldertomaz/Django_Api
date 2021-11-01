from django.db import models
from django.contrib.auth.models import User






class Silo(models.Model):
    

    silo_mac = models.CharField(max_length=500, blank=True, null=True)
    weight = models.FloatField(default=0, blank=True, null=True)
    datetime_fetched = models.DateTimeField( null=True, blank=True)
    