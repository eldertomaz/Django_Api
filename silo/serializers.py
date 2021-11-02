from django.db.models.aggregates import Sum
from rest_framework import serializers


from .models import Silo

class SiloSerializer(serializers.ModelSerializer):
    #total_silo = serializers.SerializerMethodField()

    class Meta:
        model = Silo
        fields = '__all__'