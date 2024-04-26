from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *
def insert_topic(request):
    tn=input()
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('topic is created successfully')
def insert_webpage(request):

    tn=input('enter tn')
    n=input('enter n')
    u=input('enter u')
    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        TO=LTO[0]
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
        WO.save()
        return HttpResponse('webpage is created')
    else:
        return HttpResponse('webpage is not created successfully')
def insert_accessrecord(request):
    n=input('enter n')
    a=input('enter a')
    d=input('enter d')
    tn=input('enter tn')
    u=input('enter u')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    AO=AcessRecord.objects.get_or_create(name=WO,date=d,author=a,)[0]
    AO.save()
    return HttpResponse('acessrecord  is created successfully')




