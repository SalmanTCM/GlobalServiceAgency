# from django.contrib import admin
# from .models import Customer
#
# admin.site.register(Customer)
from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('pax_first_name', 'pax_last_name', 'passport_no', 'pnr_no', 'email', 'phone_number', 'travel_date', 'address')
    list_filter = ('travel_date',)  # Optional: Add filters
    search_fields = ('pax_first_name', 'pax_last_name', 'passport_no', 'pnr_no', 'email')  # Optional: Add search fields

# Register the admin class with your model
admin.site.register(Customer, CustomerAdmin)
