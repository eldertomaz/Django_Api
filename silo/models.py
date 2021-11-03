from django.db import models
from django.contrib.auth.models import User


class Silo(models.Model):
    
    silo_mac = models.CharField(max_length=500)
    #weight = models.FloatField(default=0, blank=True, null=True)
    #datetime_fetched = models.DateTimeField( null=True, blank=True)
    
    def __str__(self):
        return self.silo_mac
class SiloFeedWeight(models.Model):

    #id = models.AutoField(primary_key=True)
    silo = models.ForeignKey(Silo, related_name='silo_feed_weights', on_delete=models.CASCADE)
    weight = models.FloatField(blank=False)
    datetime_fetched = models.DateTimeField(blank=False)


    