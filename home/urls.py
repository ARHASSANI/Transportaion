from django.urls import path
from home.views import TransportView,CartypeView,shipmentView,CarsView,reportView

urlpatterns =[
    path('transport/', TransportView.as_view()),
    path('cartype/', CartypeView.as_view()), 
    path('shipment/', shipmentView.as_view()), 
    path('cars/', CarsView.as_view()), 
    path('report/', reportView.as_view()), 

]


