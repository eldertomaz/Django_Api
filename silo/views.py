from django.db.models.aggregates import Sum
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Silo
from .serializers import SiloSerializer
from django.http import HttpResponse, response
from django_filters import rest_framework as filters




class SiloExtra(viewsets.ModelViewSet):
    

    queryset = Silo.objects.all()
    serializer_class = SiloSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

    def list(self, request, *args, **kwargs):
        #queryset = self.queryset
        start_date = self.request.data.get('start')
        end_date = self.request.data.get('end')
        if(start_date and end_date):
            silo_date = self.queryset.filter(datetime_fetched__gte = start_date, datetime_fetched__lte = end_date).order_by('datetime_fetched')
            total_weight = silo_date.aggregate(Sum('weight')).get('weight__sum') or 0.00
            #silo_date.filter(None != self.queryset.weight )
            silo_date =silo_date.exclude(weight__isnull=True)
            total =silo_date[0].weight-silo_date.last().weight
            print(total) 
            total={"total":total}
            return response.JsonResponse(total)
            #query_set = queryset.filter() date__range=["2021-01-01", "2031-01-01"]
            #return query_set()
        print(self.get_queryset())
        return response.HttpResponseServerError({'Adicionar as datas de inicio(start) e fim(end) como parametro'})

class SiloList(viewsets.ModelViewSet):
    queryset = Silo.objects.all()
    serializer_class = SiloSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
    def get_queryset(self):
        return super().get_queryset()
