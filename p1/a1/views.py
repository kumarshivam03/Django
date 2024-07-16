from django.shortcuts import render
from django.http import HttpResponse

import datetime

def currDate(request):
    now=datetime.datetime.now()
    html="<html><body>It is now %s.</body></html>"%now
    return HttpResponse(html)

def afterDate(request):
    now=datetime.datetime.now()+datetime.timedelta(hours=4)
    html="<html><body>It is now %s.</body></html>"%now
    return HttpResponse(html)

def beforeDate(request):
    now=datetime.datetime.now()+datetime.timedelta(hours=-4)
    html="<html><body>It is now %s.</body></html>"%now
    return HttpResponse(html)