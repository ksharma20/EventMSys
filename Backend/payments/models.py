from django.db import models
from events.models import Event

# Create your models here.
class Checkout(models.Model):
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    mobile = models.IntegerField( null=True )
    email = models.EmailField(max_length=254, null=True)
    address = models.TextField( null=True )
    pin_code = models.IntegerField( null=True )
    paid = models.BooleanField( default= False )
    amount = models.IntegerField( default= 0 )
    order_at = models.DateTimeField( auto_now=True )

    def __str__(self):
        return "Rs "+str(self.amount)+" at "+str(self.order_at.date())
    