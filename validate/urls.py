from django.urls import path
from . import views

urlpatterns = [
    path('validate', views.val),
    path('<str:MerchID>/<str:BranchID>/<str:platform>/<int:months>', views.topup),
] 
