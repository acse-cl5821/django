from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, timedelta
import json
from .models import Order
from urllib.request import urlopen
import random


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
    #TGId += data['store']['id']
    TGId += date.today().strftime("%y%m%d")
    TGId += platform
    TGId += str(random.randint(0,100000))
    new_order = Order(TGId=TGId, Order_id=data['order_id'], Platform=platform, Displayed_id=data['displayed_id'], Cart=json.dumps(data['cart'],ensure_ascii=False), Placed_at=data['placed_at'], Branch_Id=data['branch_id'], Merch_Id=data['merch_id'], Price=round(float(data['price']),2))
    new_order.save()
    return HttpResponse(json.dumps(dict(TGId=TGId)))


def getOrders(request):
    if request.method == 'GET':
        return HttpResponse("Please use POST request")
    data = json.loads(request.body.decode('utf-8'))
    obj = Order.objects.filter(Merch_Id = data['merch_id'], Branch_Id = data['branch_id'])[-50:]
    result = dict()
    orders = []
    for o in obj:
        order = dict()
        order['merch_id'] = data['merch_id']
        order['branch_id'] = data['branch_id']
        order['platform'] = o.Platform
        order['order_id'] = o.Displayed_id
        order['placed_at'] = str(o.Placed_at)[:-6]
        order['price'] = o.Price
        orders.append(order)
    orders = orders[::-1]
    result['total'] = len(orders)
    result['users'] = orders
    return HttpResponse(json.dumps(result))


def getNums(request, merchname, branchname, startdate, enddate):
    from datetime import date
    start_date = date(int(startdate.split('-')[0]), int(startdate.split('-')[1]), int(startdate.split('-')[2]))
    end_date = date(int(enddate.split('-')[0]), int(enddate.split('-')[1]), int(enddate.split('-')[2]))
    delta = end_date - start_date
    date_to_loop = []
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        date_to_loop.append(day)

    result = dict()
    data = []
    for date in date_to_loop:
        obj = Order.objects.filter(Merch_Id = merchname, Branch_Id = branchname, Placed_at__contains=str(date))
        hp, dr, ue, ft, total = 0, 0, 0, 0, 0
        for o in obj:
            total += 1
            if o.Platform == "01":
                hp += 1
            if o.Platform == "02":
                dr += 1
            if o.Platform == "03":
                ue += 1
            if o.Platform == "04":
                ft += 1
        row = dict()
        row['\u65e5\u671f'] = str(date)
        row['\u603b\u5355\u91cf'] = total
        row['HungryPanda'] = hp
        row['Deliveroo'] = dr
        row['UberEats'] = ue
        row['Fantuan'] = ft
        data.append(row)
    result['data'] = data
    return HttpResponse(json.dumps(result))



def getPrices(request, merchname, branchname, startdate, enddate):
    from datetime import date
    start_date = date(int(startdate.split('-')[0]), int(startdate.split('-')[1]), int(startdate.split('-')[2]))
    end_date = date(int(enddate.split('-')[0]), int(enddate.split('-')[1]), int(enddate.split('-')[2]))
    delta = end_date - start_date
    date_to_loop = []
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        date_to_loop.append(day)

    result = dict()
    data = []
    for date in date_to_loop:
        obj = Order.objects.filter(Merch_Id = merchname, Branch_Id = branchname, Placed_at__contains=str(date))
        hp, dr, ue, ft, total = 0, 0, 0, 0, 0
        for o in obj:
            total += o.Price
            if o.Platform == "01":
                hp += o.Price
            if o.Platform == "02":
                dr += o.Price
            if o.Platform == "03":
                ue += o.Price
            if o.Platform == "04":
                ft += o.Price
        row = dict()
        row['\u65e5\u671f'] = str(date)
        row['\u603b\u91d1\u989d'] = total
        row['HungryPanda'] = hp
        row['Deliveroo'] = dr
        row['UberEats'] = ue
        row['Fantuan'] = ft
        data.append(row)
    result['data'] = data
    return HttpResponse(json.dumps(result))


def heat(request, merchname, branchname, startdate, enddate):
    from datetime import date
    start_date = date(int(startdate.split('-')[0]), int(startdate.split('-')[1]), int(startdate.split('-')[2]))
    end_date = date(int(enddate.split('-')[0]), int(enddate.split('-')[1]), int(enddate.split('-')[2]))
    delta = end_date - start_date
    date_to_loop = []
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        date_to_loop.append(day)

    result = dict()
    data = []
    data2 = []
    for date in date_to_loop:
        for h in range(24,7,-1):
            if h < 10:
                h = "0" + str(h)
            else:
                h = str(h)
            obj = Order.objects.filter(Merch_Id = merchname, Branch_Id = branchname, Placed_at__contains=str(date) + " " +h)
            num, price = 0, 0
            for o in obj:
                num += 1
                price += o.Price
            row = dict()
            row['\u65e5\u671f'] = str(date)
            row['\u65f6\u95f4'] = h+":00"
            row['\u8425\u4e1a\u989d'] = price
            data.append(row)
            row = dict()
            row['\u65e5\u671f'] = str(date)
            row['\u65f6\u95f4'] = h+":00"
            row['\u5355\u91cf'] = num
            data2.append(row)

            
    result['data'] = data
    result['data2'] = data2
    return HttpResponse(json.dumps(result))


