from django.contrib import admin
from .models import Customer, salesLog
from rangefilter.filters import DateRangeFilter
from django.utils.safestring import mark_safe
from django.utils.html import format_html

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'passport_no', 'email', 'phone_number', 'address', 'booking_type', 'file', 'display_image')
    list_filter = ('booking_type', 'passport_no')
    search_fields = ('pax_first_name', 'pax_last_name', 'passport_no', 'pnr_no', 'email')

    def display_image(self, obj):
        if obj.file:
            return mark_safe(f'<img src="{obj.file.url}" width="50" height="50" />')
        return "No Image"



admin.site.register(Customer, CustomerAdmin)


class SalesLogAdmin(admin.ModelAdmin):
    list_display = (
        'customer', 'agent_name', 'ticket_no', 'pnr_no', 'route', 'travel_date', 'base_fare', 'tax', 'discount',
        'customer_price',
        'payment_method', 'remarks', 'date_of_issue', 'issue_types', 'penalty', 'refund_price', 'service_charge'
    )
    list_editable = ('discount',)
    # list_filter = (("travel_date", DateRangeFilter),)
    search_fields = ('agent_id', 'ticket_no', 'pnr_no', 'route', 'remarks')

class Media:
    js = ('Customer/admin/js/sales_log_admin.js',)


def issue_types_colored(self, obj):
    color = 'green' if obj.issue_types == 'no_issue' else 'red'
    return format_html('<span style="color: {};">{}</span>', color, obj.issue_types)
    issue_types_colored.short_description = 'Issue Types'


admin.site.register(salesLog, SalesLogAdmin)

