from rest_framework import serializers
from .models import Silo

class SiloSerializer(serializers.ModelSerializer):

    class Meta:
        model = Silo
        fields = '__all__'