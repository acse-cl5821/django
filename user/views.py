from django.shortcuts import render
import json
# Create your views here.

def login(request):
    data = json.loads(request .body.decode('utf-8'))
    obj = Validate.objects.filter (MerchID = data['username'], BranchID = data['branchname'])
    result = dict()
    if len(obj) <= 0:
        result['code'] = 404
    elif data['password'] != data['branchname']+'1001':
        result['code'] = 404
    else:
        result['code'] = 0
        result['name'] = data['branchname']
        result['roles'] = [data['branchname']]
        result['token'] = data['branchname']
    return HttpResponse(json.dumps(result))

def logout(request):
    data = {
      code: 0,
      Message: 'success'
    }
    return HttpResponse(json.dumps(data))
