from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "title": "GATES 2020 | GTBIT Official Techno-Cultural Fest Event for creative Souls",
    }
    return render(request,"index.html",context)

def about(request):
    context = {

    }
    return render(request,"about.html",context)

def developer(request):
    context = {

    }
    return render(request,"developer.html",context)

def starNight(request):
    context = {

    }
    return render(request,"starNight.html",context)