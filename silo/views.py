from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Silo
from .serializers import SiloSerializer
from django.http import HttpResponse


class SiloList(viewsets.ModelViewSet):

    queryset = Silo.objects.all()
    serializer_class = SiloSerializer
    # def get_queryset(self):
    #     return super().get_queryset()
