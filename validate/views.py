from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.shortcuts import redirect
from .models import Validate
import json
import datetime as dt
from datetime import datetime

# Create your views here.
def val(request):
    #if request.method == 'GET':
        #return HttpResponse("Please use POST request")
    data = json.loads(request.body.decode('utf-8'))
    obj = Validate.objects.filter(MerchID = data['MerchID'], BranchID = data['BranchID'])
    if len(obj) <= 0:
        data = dict()
        data['code'] = 200
        data['message'] = "Merch or Branch doesn't exist"
        return HttpResponse(json.dumps(data))
    else:
        obj = obj[0]
    data = dict()
    data['code'] = 0
    data['ValidUntil'] = obj.ValidUntil.strftime("%Y-%m-%d")
    data['HungryPanda'] = obj.HungryPanda
    if obj.HP_Valid != None:
        data['HP_Valid'] = obj.HP_Valid.strftime("%Y-%m-%d")
    data['Deliveroo'] = obj.Deliveroo
    if obj.DR_Valid != None:
        data['DR_Valid'] = obj.DR_Valid.strftime("%Y-%m-%d")
    data['UberEats'] = obj.UberEats
    if obj.UE_Valid != None:
        data['UE_Valid'] = obj.UE_Valid.strftime("%Y-%m-%d")
    data['Fantuan'] = obj.Fantuan
    if obj.FT_Valid != None:
        data['FT_Valid'] = obj.FT_Valid.strftime("%Y-%m-%d")
    return HttpResponse(json.dumps(data))


def test(request):
    with open('test.txt', 'w') as f:
        f.write("123")
    return HttpResponse("123")


def increase_month(d, month):
    if d == None:
        d = dt.date.today()
    month += d.month
    if month > 12:
        month -= 12
        year = d.year + 1
    else:
        year = d.year
    day = d.day
    try:
        res = dt.date(year=year, month=month, day=day)
    except:
        try:
            res = dt.date(year=year, month=month, day=30)
        except:
            res = dt.date(year=year, month=month, day=28)
    return res


def topup(request, MerchID, BranchID, platform, months):
    obj = Validate.objects.get(MerchID = MerchID, BranchID = BranchID)
    if platform == 'HungryPanda':
        d = obj.HP_Valid
        d = increase_month(d,months)
        obj.HP_Valid = d
        obj.save()
    if platform == 'Deliveroo':
        d = obj.DR_Valid
        d = increase_month(d,months)
        obj.DR_Valid = d
        obj.save()
    if platform == 'UberEats':
        d = obj.UE_Valid
        d = increase_month(d,months)
        obj.UE_Valid = d
        obj.save()
    if platform == 'Fantuan':
        d = obj.FT_Valid
        d = increase_month(d,months)
        obj.FT_Valid = d
        obj.save()
    return redirect("http://localhost:9528")

def download(request):
    def file_iterator(file_name, chunk_size=512):
        with open(file_name, "rb") as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = "AutoIn.exe"
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response 
