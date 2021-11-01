from django.shortcuts import render
from rest_framework import generics
from .models import Silo
from .serializers import SiloSerializer
from django.http import HttpResponse


class SiloList(generics.ListCreateAPIView):

    queryset = Silo.objects.all()
    serializer_class = SiloSerializer
