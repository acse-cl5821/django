from django.http import HttpResponse
from urllib.request import urlopen
import json
import requests


def version(request):
    version = "1.0.5"
    return HttpResponse(version)

def version_info(request):
    message = "Update Info v1.0.5:\n2023-3-17  UberEats updates their website structure, this version update our method to detect UberEats orders."
    #return HttpResponse(message.encode('unicode_escape').strip())
    return HttpResponse(message)


def amazon(request):
    return HttpResponse(urlopen('https://www.amazon.co.jp/s?k=%E3%81%BB%E3%81%BC%E6%97%A5+weeks&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=3OU2NRJEPQ6&sprefix=%E3%81%BB%E3%81%BC%E6%97%A5+weeks%2Caps%2C283&ref=nb_sb_noss_1'))

def amazon1(request):
    return HttpResponse(urlopen('https://www.amazon.co.jp/s?k=%E3%81%BB%E3%81%BC%E6%97%A5+%E3%81%86%E3%81%95%E3%81%8E&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=IEL36LK8I5TC&sprefix=%E3%81%BB%E3%81%BC%E6%97%A5+hon%2Caps%2C630&ref=nb_sb_noss_1'))

def amazon2(request):
    print("12344")