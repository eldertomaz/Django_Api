from django.conf.urls import url
from . import views

urlpatterns = [
    #POST
    url(r'^silo_feed_acquisition/', views.SiloList.as_view({'post': 'create'}), name='silo-list'),
    #GET
    url(r'^silo_feed_weight/', views.SiloList.as_view({'get': 'list'}), name='silo-list'),
    #GET SILO POR DATA
    url(r'^silo_extra/', views.SiloList.as_view({'get': 'list'}), name='silo-list'),

]

