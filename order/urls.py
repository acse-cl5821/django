from django.urls import path
from . import views

urlpatterns = [
    path('new', views.new),
    path('getOrders', views.getOrders),
    path('num/<str:merchname>/<str:branchname>/<str:startdate>/<str:enddate>', views.getNums),
    path('price/<str:merchname>/<str:branchname>/<str:startdate>/<str:enddate>', views.getPrices),
    path('heat/<str:merchname>/<str:branchname>/<str:startdate>/<str:enddate>', views.heat),
]
