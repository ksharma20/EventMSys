from django.contrib import admin
from .models import Checkout

# Register your models here.
class Checkout_Filter(admin.ModelAdmin):
    list_display = ("pk", "email", "mobile", "amount", "paid", "order_at", "pin_code")
    list_filter = ("paid", "order_at")

admin.site.register(Checkout, Checkout_Filter)