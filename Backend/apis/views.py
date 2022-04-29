# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EventDate, Event, EDatesSerializer, EventSerializer

# Create your views here.
@api_view(["GET"])
def events(request):
    event = Event.objects.all()
    es = EventSerializer(event, many=True)
    return Response(es.data)

@api_view(["GET"])
def eventDates(request, id):
    edates = EventDate.objects.filter(event=id)
    eds = EDatesSerializer(edates, many=True)
    return Response(eds.data)
