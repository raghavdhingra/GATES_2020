"""gates2020 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import main.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("event/",views.event,name="event"),
    path("event/technical/",views.techEvent,name="technical"),
    path("event/cultural/",views.culturalEvent,name="cultural"),
    path("event/miscellaneous/",views.miscEvent,name="miscellaneous"),
    path("event/divine/",views.divineEvent,name="divine"),
    path("event/management/",views.manageEvent,name="management"),
    path("developer/",views.developer,name="developer"),
    path("star-night/",views.starNight,name="starNight"),
]
