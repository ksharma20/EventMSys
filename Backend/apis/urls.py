import imp
from django.urls import path, include
from .views import events, eventDates

app_name = "apis"

urlpatterns = [
    path('auth/', include("rest_framework.urls", "rest_framework")),
    path('events', events),
    path('event/<id>', eventDates),
]
