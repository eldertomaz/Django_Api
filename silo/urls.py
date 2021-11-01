from django.conf.urls import url
from . import views

urlpatterns = [
    #POST
    url(r'^silo_feed_acquisition/', views.SiloList.as_view(), name='silo-list'),
    #GET
    url(r'^silo_feed_weight/<int:id>', views.SiloList.as_view(), name='silo-list'),

]

