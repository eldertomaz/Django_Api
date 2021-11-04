from django.db.models.aggregates import Sum
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Silo, SiloFeedWeight
from .serializers import SiloFeedWeightSerializer, SiloSerializer
from django.http import HttpResponse, response
from django_filters import rest_framework as filters




class SiloExtra(viewsets.ModelViewSet):
    

    queryset = SiloFeedWeight.objects.all()
    serializer_class = SiloFeedWeightSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

    def list(self, request, *args, **kwargs):
        #queryset = self.queryset
        start_date = self.request.GET.get("start")#self.request.data.get('start')
        end_date = self.request.GET.get("end")#self.request.data.get('end')
        api_silo=self.request.GET.get("silo")
        if(api_silo):
            if(start_date and end_date):
                silo_date = self.queryset.filter(silo=api_silo,datetime_fetched__gte = start_date, datetime_fetched__lte = end_date).order_by('datetime_fetched')
                #total_weight = silo_date.aggregate(Sum('weight')).get('weight__sum') or 0.00
            #     #silo_date.filter(None != self.queryset.weight )
                silo_date =silo_date.exclude(weight__isnull=True)
                total =silo_date[0].weight-silo_date.last().weight 
                total={"total":total}
                return response.JsonResponse(total)
            #     #query_set = queryset.filter() date__range=["2021-01-01", "2031-01-01"]
            #     #return query_set()
            #print(self.get_queryset())
            else:
                return response.HttpResponseServerError({'Adicionar as datas de inicio(start) e fim(end) como parametro'})
        return response.HttpResponseServerError({'informar id do silo'})        

class SiloViews(viewsets.ModelViewSet):
    queryset = Silo.objects.all()
    serializer_class = SiloSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
    def get_queryset(self):
        return super().get_queryset()

class SiloWeightViews(viewsets.ModelViewSet):
    queryset = SiloFeedWeight.objects.all()
    serializer_class = SiloFeedWeightSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
    lookup_url_kwarg = "silo"
    def get_queryset(self):
        print(self.request.GET.get("start"))
        return super().get_queryset()
    