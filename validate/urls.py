from django.urls import path
from . import views

urlpatterns = [
    path('validate', views.val),
    path('download', views.download),
    path('test', views.test),
    path('<str:MerchID>/<str:BranchID>/<str:platform>/<int:months>', views.topup),
] 
