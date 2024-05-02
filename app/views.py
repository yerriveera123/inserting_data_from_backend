from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *
from django.db.models.functions import Length
def insert_topic(request):
    tn=input()
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    d={'QLTO':Topic.objects.all()}

    return render(request,'display_topics.html',d)
def insert_webpage(request):

    tn=input('enter tn')
    n=input('enter n')
    u=input('enter u')
    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        TO=LTO[0]
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
        WO.save()
        d={'QLWO':Webpage.objects.all()}

        return render(request,'display_webpage.html',d)
    else:
        return HttpResponse('webpage is not created successfully')
def insert_accessrecord(request):
    '''
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
    '''
    i=int(input('enter id of webpage object'))
    a=input('enter a')
    d=input('enter d')
    WO=Webpage.objects.get(id=i)
    AO=AcessRecord.objects.get_or_create(name=WO,date=d,author=a,)[0]
    AO.save()
    d={'QLAO':AcessRecord.objects.all()}

    return render(request,'display_accessrecord.html',d)
def display_topics(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topics.html',d)
def display_webpage(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(topic_name='cricket')
    QLWO=Webpage.objects.exclude(topic_name='cricket')
    QLWO=Webpage.objects.all()[::-1]
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.all().order_by('-name')
    QLWO=Webpage.objects.all().order_by(Length('name'))
    QLWO=Webpage.objects.all().order_by(Length('name').desc())
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)
def display_accessrecord(request):
    QLAO=AcessRecord.objects.all()
    d={'QLAO':QLAO}
    return render(request,'display_accessrecord.html',d)

