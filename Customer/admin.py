from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'passport_no', 'pnr_no', 'email', 'phone_number', 'travel_date', 'address', 'booking_type')  # Add 'booking_type' to the list display
    list_filter = ('travel_date', 'booking_type')  # Add 'booking_type' to the list filter
    search_fields = ('pax_first_name', 'pax_last_name', 'passport_no', 'pnr_no', 'email')  # Optional: Add search fields

# Register the admin class with your model
admin.site.register(Customer, CustomerAdmin)
