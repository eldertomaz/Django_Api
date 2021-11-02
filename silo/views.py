from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Silo
from .serializers import SiloSerializer
from django.http import HttpResponse
from django_filters import rest_framework as filters



class SiloList(viewsets.ModelViewSet):

    queryset = Silo.objects.all()
    serializer_class = SiloSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    #filter_class = filter  
    filter_fields = '__all__'
    def get_queryset(self):
        queryset = self.queryset
        start_date = self.request.data.get('start')
        end_date = self.request.data.get('end')
        if(self.request.path == '/silo_extra/' and start_date and end_date):
            print('aqui')
            print(start_date)
            print(end_date)
            print('fim')
            return queryset.filter(datetime_fetched__gte = start_date, datetime_fetched__lte = end_date)
        return super().get_queryset()
    
