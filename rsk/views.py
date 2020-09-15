from django.shortcuts import render,redirect
from django.http import HttpResponse
from rsk.models import *

def create_topic(request):
    if request.method=="POST":
        topic=request.POST.get("topic")
        t=Topic.objects.get_or_create(topic_name=topic)
        if t[1]==True:
            t[0].save()
            return HttpResponse("<h3>Topic added successfully")
        else:
            return HttpResponse("<h3>Topic Is Already Exist In Table</h3>")
    return render(request,"create_topic.html")

def create_webpage(request):
    if request.method=="POST":
        topic=request.POST.get('topic')
        name=request.POST.get('name')
        url=request.POST.get("url")
        t=Topic.objects.get_or_create(topic_name=topic)[0]
        w=Webpage.objects.get_or_create(topic=t,name=name,url=url)[0]
        w.save()
        return HttpResponse("<h3>Webpage Added Successfully</h3>")
    topics=Topic.objects.all()
    return render(request,"create_Webpage.html",context={'topics':topics})

def display_topics(request):
    topics=Topic.objects.all()
    return render(request,"display_topic.html",context={'topics':topics})

def display_topic(request,id):
    topics=Topic.objects.filter(id=id)
    return render(request,"display_topic.html",context={'topics':topics})


def display_webpages(request):
    webpages=Webpage.objects.all()
    return render(request,"display_webpage.html",context={'webpages':webpages})

def display_webpage(request,webid):
    webpages=Webpage.objects.filter(id=webid)
    return render(request,"display_webpage.html",context={'webpages':webpages})
    
def search_webpage(request):
    if request.GET.get('search'):
        id=request.GET['search']
        return redirect('display_webpage',webid=id)
    return render(request,'search_webpage.html')

def update_topic(request,id):
    if request.method=="POST":
        new_tname=request.POST.get("topic_name")
        t=Topic.objects.filter(id=id).update(topic_name=new_tname)
    t=Topic.objects.get(id=id)
    return render(request,"update_topic.html",{"topic":t})

def update_webpage(request,id):
    if request.method=="POST":
        topic=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        t=Topic.objects.get(topic_name=topic)
        w=Webpage.objects.filter(id=id).update(topic=t,name=name,url=url)
    t=Topic.objects.all()
    webpage=Webpage.objects.get(id=id)
    return render(request,"update_webpage.html",{"topics":t,'webpage':webpage})

def delete_topic(request,id):
    t=Topic.objects.filter(id=id)
    if t:
        t.delete()
        return HttpResponse("<h3>deletion is duccessful</h3>")
    return HttpResponse("<h3>Record not found</h3>")