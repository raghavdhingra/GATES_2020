from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import json
import requests

# Create your views here.
def home(request):
    context = {
        "title": "GATES 2020 | GTBIT Official Techno-Cultural Fest Event for creative Souls",
    }
    return render(request,"index.html",context)

def about(request):
    context = {
        "title": "ABOUT | GATES 2020",
    }
    return render(request,"about.html",context)

def developer(request):
    context = {
        "title": "Raghav Dhingra | Developer | GATES 2020",
    }
    return render(request,"developer.html",context)

def starNight(request):
    context = {
        "title": "STAR NIGHT | GATES 2020",
    }
    return render(request,"starNight.html",context)

def event(request):
    return redirect("/#event")

def getEvents(category,ImageUrl):
    new_event_list = []
    resp_data = requests.get("https://spreadsheets.google.com/feeds/list/1k315nuVJP8X6r8Cp2ANHbJEt1kXyp55s6WKHed8SlNY/1/public/full?alt=json")
    resp = json.loads(resp_data.text)
    event_list = resp["feed"]["entry"]
    for event in event_list:
        new_event = {}
        if event["gsx$eventcategory"]["$t"] == category:
            new_event["name"] = event["gsx$eventname"]["$t"]
            new_event["description"] = event["gsx$eventdescription"]["$t"]
            new_event["day"] = event["gsx$eventday"]["$t"]
            new_event["timing"] = event["gsx$eventtimings"]["$t"]
            new_event["duration"] = event["gsx$eventduration"]["$t"]
            new_event["category"] = event["gsx$eventcategory"]["$t"]
            new_event["link"] = event["gsx$registrationlink"]["$t"]
            if event["gsx$eventimageurl"]["$t"] == "":
                new_event["imageUrl"] = ImageUrl
            else:
                new_event["imageUrl"] = event["gsx$eventimageurl"]["$t"]
            new_event_list.append(new_event)
    return new_event_list

def techEvent(request):
    context = {
        "title": "Technical Events | GATES 2020",
    }
    event_list = getEvents("Technical","/static/assets/images/technical.jpg")
    context["events"] = event_list
    context["category"] = "Technical"
    return render(request,"event.html",context)

def manageEvent(request):
    context = {
        "title": "Management Events | GATES 2020",
    }
    event_list = getEvents("Management","/static/assets/images/manage.jpg")
    context["events"] = event_list
    context["category"] = "Management"
    return render(request,"event.html",context)

def divineEvent(request):
    context = {
        "title": "Divine Events | GATES 2020",
    }
    event_list = getEvents("Divine","/static/assets/images/divine.jpg")
    context["events"] = event_list
    context["category"] = "Divine"
    return render(request,"event.html",context)

def miscEvent(request):
    context = {
        "title": "Miscellaneous Events | GATES 2020",
    }
    event_list = getEvents("Miscellaneous","/static/assets/images/misc.jpg")
    context["events"] = event_list
    context["category"] = "Miscellaneous"
    return render(request,"event.html",context)

def culturalEvent(request):
    context = {
        "title": "Cultural Events | GATES 2020",
    }
    event_list = getEvents("Cultural","/static/assets/images/cultural.jpg")
    context["events"] = event_list
    context["category"] = "Cutural"
    return render(request,"event.html",context)