# from django.contrib import admin
# from .models import salesLog
#
# admin.site.register(salesLog)
from django.contrib import admin
from .models import salesLog
from rangefilter.filters import DateRangeFilter

class SalesLogAdmin(admin.ModelAdmin):
    list_display = ('customer', 'route', 'ticket_no', 'total', 'received', 'status', 'remains', 'sale_date',)
    list_filter = ('customer', 'status', ('sale_date', DateRangeFilter),)  # Optional: Add filters
    search_fields = ('customer__phone_number',)  # Optional: Add search fields

# Register the admin class with your model
admin.site.register(salesLog, SalesLogAdmin)
