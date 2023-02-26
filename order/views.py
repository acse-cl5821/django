from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import json
from .models import Order
from urllib.request import urlopen

def new(request):
    if request.method == 'GET':
        return HttpResponse("Please use POST request")
    data = json.loads(request.body.decode('utf-8'))
    platform = "00"
    if data['platform'] == 'hungrypanda':
        platform = "01"
    elif data['platform'] == 'deliveroo':
        platform = "02"
    elif data['platform'] == 'ubereats':
        platform = "03"
    elif data['platform'] == 'fantuan':
        platform = "04"
    TGId = ""
    TGId += data['store']['id']
    TGId += platform
    TGId += date.today().strftime("%y%m%d")
    TGId += "0001"
    platform = "00"
    if data['platform'] == 'hungrypanda':
        platform = "01"
    elif data['platform'] == 'deliveroo':
        platform = "02"
    elif data['platform'] == 'ubereats':
        platform = "03"
    elif data['platform'] == 'fantuan':
        platform = "04"
    new_order = Order(TGId=TGId, Order_id=data['id'], Platform=platform, Displayed_id="", Current_state="", Cart=json.dumps(data['cart'],ensure_ascii=False), Store_id=data['store']['id'], Placed_at=data['placed_at'])
    new_order.save()
    return HttpResponse(json.dumps(dict(TGId=TGId)))


