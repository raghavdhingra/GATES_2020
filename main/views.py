from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "title": "GATES 2020 | GTBIT Official Techno-Cultural Fest Event for creative Souls",
    }
    return render(request,"index.html",context)