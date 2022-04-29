from django.db import models
from django.urls import reverse


# Create your models here.
class Event(models.Model):

    name = models.CharField( max_length=100 )
    image = models.FileField( upload_to="events/", max_length=100)
    about = models.TextField()
    price = models.IntegerField()
    req_name = models.BooleanField( default=False )
    req_email = models.BooleanField( default=False )
    req_mobile = models.BooleanField( default=False )
    req_addr = models.BooleanField( default=False )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Event_detail", kwargs={"pk": self.pk})

class EventDate(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateField( auto_now=False, auto_now_add=False)
    start_time = models.TimeField( auto_now=False, auto_now_add=False)
    end_time = models.TimeField( auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.event.name[:7]+f" {self.date}"

    def get_absolute_url(self):
        return reverse("EventDate_detail", kwargs={"pk": self.pk})
