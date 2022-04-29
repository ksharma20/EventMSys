import imp
from rest_framework import serializers
from events.models import Event,EventDate

# Serializers define the API representation.
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['pk','name','image','about','price', 'req_addr', 'req_mobile', 'req_name', 'req_email']

class EDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDate
        fields = ['event', 'date', 'start_time', 'end_time']