from django.db.models.aggregates import Sum
from rest_framework import serializers


from .models import Silo, SiloFeedWeight

class SiloSerializer(serializers.ModelSerializer):
    #total_silo = serializers.SerializerMethodField()

    class Meta:
        model = Silo
        fields = '__all__'

class SiloFeedWeightSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiloFeedWeight
        fields = '__all__'