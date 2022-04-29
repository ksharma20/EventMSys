from django.contrib import admin
from events.models import Event, EventDate

# Register your models here.
admin.site.register(Event)
admin.site.register(EventDate)