# ticket_management/admin.py

from django.contrib import admin
from .models import Customer, salesLog

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('pax_first_name', 'pax_last_name', 'passport_no', 'pnr_no', 'email', 'phone_number', 'travel_date', 'address')
    list_filter = ('travel_date',)
    search_fields = ('pax_first_name', 'pax_last_name', 'passport_no', 'pnr_no', 'email')

@admin.register(salesLog)
class SalesLogAdmin(admin.ModelAdmin):
    list_display = ('customer', 'route', 'ticket_no', 'total', 'received', 'status', 'remains', 'sale_date')
    list_filter = ('sale_date',)
    search_fields = ('customer__pax_first_name', 'customer__pax_last_name', 'route', 'ticket_no', 'status')
