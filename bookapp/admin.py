from django.contrib import admin

# Register your models here.
from bookapp.models import Customer, CustomerAdmin, Booking, BookingAdmin

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Booking,BookingAdmin)

admin.site.site_header='online train ticket booking'